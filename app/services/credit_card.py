from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import CreditCard
from app.repositories import CreditCardRepository
from app.schemas import CreditCardCreateRequest, CreditCardDTO, CreditCardUpdateRequest
from app.utilities import ModelMapper


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def get_all_credit_cards(self) -> list[CreditCardDTO]:
        credit_cards = self.repository.get_all()
        if not credit_cards:
            return []
        return ModelMapper.from_model_list(credit_cards, CreditCardDTO)

    def get_credit_cards_by_user_id(self, user_id: int) -> list[CreditCardDTO]:
        credit_cards = self.repository.get_all_by_user_id(user_id)
        if not credit_cards:
            return []
        return ModelMapper.from_model_list(credit_cards, CreditCardDTO)

    def get_credit_card_by_id(self, id: int) -> CreditCardDTO:
        credit_card = self.repository.get_by_id(id)
        if not credit_card:
            raise NotFoundError(f"Credit card with {id} id not found.")
        return ModelMapper.from_model(credit_card, CreditCardDTO)

    def create_credit_card(self, request: CreditCardCreateRequest) -> CreditCardDTO:
        try:
            credit_card = ModelMapper.from_schema(request, CreditCard)
            created = self.repository.insert(credit_card)
            return ModelMapper.from_model(created, CreditCardDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def update_credit_card(self, request: CreditCardUpdateRequest) -> CreditCardDTO:
        try:
            credit_card = self.repository.get_by_id(request.id)
            if not credit_card:
                raise NotFoundError(f"Credit card with {request.id} id not found.")

            credit_card.user_id = request.user_id
            credit_card.name = request.name
            credit_card.current_balance = request.current_balance
            credit_card.apr = request.apr
            credit_card.credit_limit = request.credit_limit

            updated = self.repository.upsert(credit_card)
            return ModelMapper.from_model(updated, CreditCardDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def delete_credit_card(self, id: int) -> bool:
        credit_card = self.repository.get_by_id(id)
        if not credit_card:
            raise NotFoundError(f"Credit card with {id} id not found.")
        return self.repository.delete(credit_card)
