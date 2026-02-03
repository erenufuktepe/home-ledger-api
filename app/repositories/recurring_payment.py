from sqlalchemy.orm import Session

from app.models.recurring_payment import RecurringPayment
from app.repositories.base import BaseRepository


class RecurringPaymentRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, RecurringPayment)
