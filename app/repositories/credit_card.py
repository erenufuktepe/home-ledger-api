from sqlalchemy.orm import Session

from app.models.credit_card import CreditCard
from app.repositories.base import BaseRepository


class CreditCardRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, CreditCard)

    def get_all_by_user_id(self, user_id: int) -> list[CreditCard]:
        return (
            self.session.query(self.model).filter(CreditCard.user_id == user_id).all()
        )
