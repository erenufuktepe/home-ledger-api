from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import RecurringPayment
from app.repositories import RecurringPaymentRepository
from app.schemas import (
    RecurringPaymentCreateRequest,
    RecurringPaymentDTO,
    RecurringPaymentUpdateRequest,
)
from app.utilities import ModelMapper


class RecurringPaymentService:
    def __init__(self, repository: RecurringPaymentRepository):
        self.repository = repository

    def get_all_recurring_payments(self) -> list[RecurringPaymentDTO]:
        recurring_payments = self.repository.get_all()
        if not recurring_payments:
            return []
        return ModelMapper.from_model_list(recurring_payments, RecurringPaymentDTO)

    def get_recurring_payment_by_id(self, id: int) -> RecurringPaymentDTO:
        recurring_payment = self.repository.get_by_id(id)
        if not recurring_payment:
            raise NotFoundError(f"Recurring payment with {id} not found.")
        return ModelMapper.from_model(recurring_payment, RecurringPaymentDTO)

    def get_recurring_payments_by_user_id(self, user_id: int) -> list[RecurringPaymentDTO]:
        recurring_payments = self.repository.get_all_by_user_id(user_id)
        if not recurring_payments:
            return []
        return ModelMapper.from_model_list(recurring_payments, RecurringPaymentDTO)

    def create_recurring_payment(self, request: RecurringPaymentCreateRequest) -> RecurringPaymentDTO:
        try:
            recurring_payment = ModelMapper.from_schema(request, RecurringPayment)
            created = self.repository.insert(recurring_payment)
            return ModelMapper.from_model(created, RecurringPaymentDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def update_recurring_payment(self, request: RecurringPaymentUpdateRequest) -> RecurringPaymentDTO:
        try:
            recurring_payment = self.repository.get_by_id(request.id)
            if not recurring_payment:
                raise NotFoundError(f"Recurring payment with {request.id} not found.")

            recurring_payment.name = request.name
            recurring_payment.category = request.category
            recurring_payment.purpose = request.purpose
            recurring_payment.frequency = request.frequency
            recurring_payment.amount = request.amount
            recurring_payment.due_day = request.due_day
            recurring_payment.due_month = request.due_month
            recurring_payment.user_id = request.user_id
            recurring_payment.account_id = request.account_id
            recurring_payment.credit_card_id = request.credit_card_id

            updated = self.repository.upsert(recurring_payment)
            return ModelMapper.from_model(updated, RecurringPaymentDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def delete_recurring_payment(self, id: int) -> bool:
        recurring_payment = self.repository.get_by_id(id)
        if not recurring_payment:
            raise NotFoundError(f"Recurring payment with {id} not found.")
        return self.repository.delete(recurring_payment)
