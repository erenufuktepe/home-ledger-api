from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
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

    def get_credit_card_by_id(self, id: int) -> CreditCardDTO:
        credit_card = self.repository.get_by_id(id)
        if not credit_card:
            raise NotFoundError(f"Credit card with {id} id not found.")
        return ModelMapper.from_model(credit_card, CreditCardDTO)

    def create_credit_card(self, request: CreditCardCreateRequest) -> bool:
        try:
            credit_cart = ModelMapper.from_schema(request, CreditCard)
            if not self.repository.insert(credit_cart):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.owner_user_id} id not found.")

    def update_credit_card(self, request: CreditCardUpdateRequest) -> bool:
        credit_card = self.repository.get_by_id(request.id)
        if not credit_card:
            raise NotFoundError(f"Credit card with {request.id} id not found.")

        credit_card.name = request.name
        credit_card.current_balance = request.current_balance

        if not self.repository.upsert(credit_card):
            return False
        return True

    def delete_credit_card(self, id: int) -> bool:
        credit_card = self.repository.get_by_id(id)
        if not credit_card:
            raise NotFoundError(f"Credit card with {id} id not found.")
        return self.repository.delete(credit_card)
