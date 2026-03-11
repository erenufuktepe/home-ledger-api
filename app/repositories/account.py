from sqlalchemy.orm import Session

from app.models.account import Account
from app.repositories.base import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Account)

    def get_all_by_user_id(self, user_id: int) -> list[Account]:
        return self.session.query(self.model).filter(Account.user_id == user_id).all()
