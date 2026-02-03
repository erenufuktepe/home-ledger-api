from app.models import CreditCard
from app.repositories import CreditCardRepository
from app.schemas import CreditCardDTO
from app.utilities import ModelMapper


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def get_all_credit_cards(self) -> list[CreditCardDTO] | None:
        credit_cards = self.repository.get_all()
        if not credit_cards:
            return None
        return ModelMapper.from_model_list(credit_cards, CreditCardDTO)

    def get_credit_card_by_id(self, id: int) -> CreditCardDTO | None:
        credit_card = self.repository.get_by_id(id)
        if not credit_card:
            return None
        return ModelMapper.from_model(credit_card, CreditCardDTO)

    def create_credit_card(self, credit_card: CreditCardDTO) -> bool:
        new_credit_card = ModelMapper.from_schema(credit_card, CreditCard)
        if not self.repository.insert(new_credit_card):
            return False
        return True

    def update_credit_card(self, credit_card: CreditCardDTO) -> bool:
        update_credit_card = ModelMapper.from_schema(credit_card, CreditCard)
        if not self.repository.upsert(update_credit_card):
            return False
        return True
