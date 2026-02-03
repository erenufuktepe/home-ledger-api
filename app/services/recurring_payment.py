from app.models import RecurringPayment
from app.repositories import RecurringPaymentRepository
from app.schemas import RecurringPaymentDTO
from app.utilities import ModelMapper


class RecurringPaymentService:
    def __init__(self, repository: RecurringPaymentRepository):
        self.repository = repository

    def get_all_recurring_payments(self) -> list[RecurringPaymentDTO] | None:
        recurring_payments = self.repository.get_all()
        if not recurring_payments:
            return None
        return ModelMapper.from_model_list(recurring_payments, RecurringPaymentDTO)

    def get_recurring_payment_by_id(self, id: int) -> RecurringPaymentDTO | None:
        recurring_payment = self.repository.get_by_id(id)
        if not recurring_payment:
            return None
        return ModelMapper.from_model(recurring_payment, RecurringPaymentDTO)

    def create_recurring_payment(self, recurring_payment: RecurringPaymentDTO) -> bool:
        new_recurring_payment = ModelMapper.from_schema(
            recurring_payment, RecurringPayment
        )
        if not self.repository.insert(new_recurring_payment):
            return False
        return True

    def update_recurring_payment(self, recurring_payment: RecurringPaymentDTO) -> bool:
        update_recurring_payment = ModelMapper.from_schema(
            recurring_payment, RecurringPayment
        )
        if not self.repository.upsert(update_recurring_payment):
            return False
        return True
