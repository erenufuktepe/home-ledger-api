from sqlalchemy.orm import Session

from app.models.loan import Loan
from app.repositories.base import BaseRepository


class LoanRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Loan)
