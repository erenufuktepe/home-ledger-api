from sqlalchemy.orm import Session

from app.models.income import Income
from app.repositories.base import BaseRepository


class IncomeRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Income)

    def get_all_by_user_id(self, user_id: int) -> list[Income]:
        return self.session.query(Income).filter(Income.user_id == user_id).all()
