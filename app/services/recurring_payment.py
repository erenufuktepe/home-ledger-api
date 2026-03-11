from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
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

    def create_recurring_payment(self, request: RecurringPaymentCreateRequest) -> bool:
        try:
            recurring_payment = ModelMapper.from_schema(request, RecurringPayment)
            if not self.repository.insert(recurring_payment):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.user_id} not found.")

    def update_recurring_payment(self, request: RecurringPaymentUpdateRequest) -> bool:
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

            if not self.repository.upsert(recurring_payment):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.user_id} not found.")

    def delete_recurring_payment(self, id: int) -> bool:
        recurring_payment = self.repository.get_by_id(id)
        if not recurring_payment:
            raise NotFoundError(f"Recurring payment with {id} not found.")
        return self.repository.delete(recurring_payment)
