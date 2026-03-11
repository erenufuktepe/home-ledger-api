from sqlalchemy.orm import Session

from app.models.account_snapshot import AccountSnapshot
from app.repositories.base import BaseRepository


class AccountSnapshotRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, AccountSnapshot)
