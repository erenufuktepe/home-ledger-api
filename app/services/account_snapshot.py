from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
from app.models import AccountSnapshot
from app.repositories import AccountSnapshotRepository
from app.schemas import (
    AccountSnapshotCreateRequest,
    AccountSnapshotDTO,
    AccountSnapshotUpdateRequest,
)
from app.utilities import ModelMapper


class AccountSnapshotService:
    def __init__(self, repository: AccountSnapshotRepository):
        self.repository = repository

    def get_all_account_snapshots(self) -> list[AccountSnapshotDTO]:
        snapshots = self.repository.get_all()
        if not snapshots:
            return []
        return ModelMapper.from_model_list(snapshots, AccountSnapshotDTO)

    def get_account_snapshot_by_id(self, id: int) -> AccountSnapshotDTO:
        snapshot = self.repository.get_by_id(id)
        if not snapshot:
            raise NotFoundError(f"Account snapshot with {id} id not found.")
        return ModelMapper.from_model(snapshot, AccountSnapshotDTO)

    def create_account_snapshot(self, request: AccountSnapshotCreateRequest) -> bool:
        try:
            snapshot = ModelMapper.from_schema(request, AccountSnapshot)
            if not self.repository.insert(snapshot):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"Account with {request.account_id} id not found.")

    def update_account_snapshot(self, request: AccountSnapshotUpdateRequest) -> bool:
        try:
            snapshot = self.repository.get_by_id(request.id)
            if not snapshot:
                raise NotFoundError(f"Account snapshot with {request.id} id not found.")

            snapshot.account_id = request.account_id
            snapshot.balance = request.balance
            snapshot.snapshot_datetime = request.snapshot_datetime

            if not self.repository.upsert(snapshot):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"Account with {request.account_id} id not found.")

    def delete_account_snapshot(self, id: int) -> bool:
        snapshot = self.repository.get_by_id(id)
        if not snapshot:
            raise NotFoundError(f"Account snapshot with {id} id not found.")
        return self.repository.delete(snapshot)
