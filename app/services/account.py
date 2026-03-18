from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import Account
from app.repositories import AccountRepository
from app.schemas import AccountCreateRequest, AccountDTO, AccountUpdateRequest
from app.utilities import ModelMapper


class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

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

    def create_account(self, request: AccountCreateRequest) -> AccountDTO:
        try:
            account = ModelMapper.from_schema(request, Account)
            created = self.repository.insert(account)
            return ModelMapper.from_model(created, AccountDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def update_account(self, request: AccountUpdateRequest) -> AccountDTO:
        try:
            account = self.repository.get_by_id(request.id)
            if not account:
                raise NotFoundError(f"Account with {request.id} id not found.")

            account.user_id = request.user_id
            account.name = request.name
            account.account_type = request.account_type
            account.balance = request.balance
            account.apy = request.apy
            account.is_joint = request.is_joint

            updated = self.repository.upsert(account)
            return ModelMapper.from_model(updated, AccountDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def delete_account(self, id: int) -> bool:
        account = self.repository.get_by_id(id)
        if not account:
            raise NotFoundError(f"Account with {id} id not found.")
        return self.repository.delete(account)
