from sqlalchemy.orm import Session

from app.models.recurring_payment import RecurringPayment
from app.repositories.base import BaseRepository


class RecurringPaymentRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, RecurringPayment)

    def get_all_by_user_id(self, user_id: int) -> list[RecurringPayment]:
        return self.session.query(RecurringPayment).filter(RecurringPayment.user_id == user_id).all()
