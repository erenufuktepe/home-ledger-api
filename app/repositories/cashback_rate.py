from sqlalchemy.orm import Session

from app.models.cashback_rate import CashbackRate
from app.repositories.base import BaseRepository


class CashbackRateRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, CashbackRate)
