from sqlalchemy.orm import Session

from app.models.credit_card import CreditCard
from app.repositories.base import BaseRepository


class CreditCardRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, CreditCard)
