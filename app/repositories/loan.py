from sqlalchemy.orm import Session

from app.models.loan import Loan
from app.repositories.base import BaseRepository


class LoanRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Loan)

    def get_all_by_user_id(self, user_id: int) -> list[Loan]:
        return self.session.query(Loan).filter(Loan.user_id == user_id).all()
