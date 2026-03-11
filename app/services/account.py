from datetime import datetime

from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
from app.models import Account, AccountSnapshot
from app.repositories import AccountRepository, AccountSnapshotRepository
from app.schemas import AccountCreateRequest, AccountDTO, AccountUpdateRequest
from app.utilities import ModelMapper


class AccountService:
    def __init__(
        self,
        repository: AccountRepository,
        account_snapshot_repository: AccountSnapshotRepository,
    ):
        self.repository = repository
        self.account_snapshot_repository = account_snapshot_repository

    def get_all_accounts(self) -> list[AccountDTO]:
        accounts = self.repository.get_all()
        if not accounts:
            return []
        return ModelMapper.from_model_list(accounts, AccountDTO)

    def get_accounts_by_user_id(self, user_id: int) -> list[AccountDTO]:
        accounts = self.repository.get_all_by_user_id(user_id)
        if not accounts:
            return []
        return ModelMapper.from_model_list(accounts, AccountDTO)

    def get_account_by_id(self, id: int) -> AccountDTO:
        account = self.repository.get_by_id(id)
        if not account:
            raise NotFoundError(f"Account with {id} id not found.")
        return ModelMapper.from_model(account, AccountDTO)

    def create_account(self, request: AccountCreateRequest) -> bool:
        try:
            account = ModelMapper.from_schema(request, Account)
            created_account = self.repository.insert(account)
            if not created_account:
                return False

            snapshot = AccountSnapshot(
                account_id=created_account.id,
                balance=created_account.balance,
                snapshot_datetime=datetime.utcnow(),
            )
            self.account_snapshot_repository.insert(snapshot)
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.user_id} id not found.")

    def update_account(self, request: AccountUpdateRequest) -> bool:
        try:
            account = self.repository.get_by_id(request.id)
            if not account:
                raise NotFoundError(f"Account with {request.id} id not found.")
            previous_balance = account.balance

            account.user_id = request.user_id
            account.name = request.name
            account.account_type = request.account_type
            account.balance = request.balance
            account.apy = request.apy
            account.is_joint = request.is_joint

            updated_account = self.repository.upsert(account)
            if not updated_account:
                return False

            if previous_balance != updated_account.balance:
                snapshot = AccountSnapshot(
                    account_id=updated_account.id,
                    balance=updated_account.balance,
                    snapshot_datetime=datetime.utcnow(),
                )
                self.account_snapshot_repository.insert(snapshot)
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.user_id} id not found.")

    def delete_account(self, id: int) -> bool:
        account = self.repository.get_by_id(id)
        if not account:
            raise NotFoundError(f"Account with {id} id not found.")
        return self.repository.delete(account)
