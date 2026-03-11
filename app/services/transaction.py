from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
from app.models import Transaction
from app.repositories import TransactionRepository
from app.schemas import (
    TransactionCreateRequest,
    TransactionDTO,
    TransactionUpdateRequest,
)
from app.utilities import ModelMapper


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def get_all_transactions(self) -> list[TransactionDTO]:
        transactions = self.repository.get_all()
        if not transactions:
            return []
        return ModelMapper.from_model_list(transactions, TransactionDTO)

    def get_transaction_by_id(self, id: int) -> TransactionDTO:
        transaction = self.repository.get_by_id(id)
        if not transaction:
            raise NotFoundError(f"Transaction with {id} id not found.")
        return ModelMapper.from_model(transaction, TransactionDTO)

    def create_transaction(self, request: TransactionCreateRequest) -> bool:
        try:
            transaction = ModelMapper.from_schema(request, Transaction)
            if not self.repository.insert(transaction):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(
                f"Recurring payment with {request.recurring_payment_id} id not found."
            )

    def update_transaction(self, request: TransactionUpdateRequest) -> bool:
        try:
            transaction = self.repository.get_by_id(request.id)
            if not transaction:
                raise NotFoundError(f"Transaction with {request.id} id not found.")

            transaction.amount = request.amount
            transaction.recurring_payment_id = request.recurring_payment_id
            transaction.transaction_datetime = request.transaction_datetime

            if not self.repository.upsert(transaction):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(
                f"Recurring payment with {request.recurring_payment_id} id not found."
            )

    def delete_transaction(self, id: int) -> bool:
        transaction = self.repository.get_by_id(id)
        if not transaction:
            raise NotFoundError(f"Transaction with {id} id not found.")
        return self.repository.delete(transaction)
