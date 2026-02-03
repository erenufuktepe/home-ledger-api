from sqlalchemy.orm import Session

from app.models.income import Income
from app.repositories.base import BaseRepository


class IncomeRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Income)
