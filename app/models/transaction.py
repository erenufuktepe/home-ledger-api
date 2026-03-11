from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.models.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    amount = Column(Numeric(12, 2), nullable=False)
    recurring_payment_id = Column(
        BigInteger, ForeignKey("recurring_payments.id"), nullable=True
    )
    transaction_datetime = Column(DateTime, nullable=False)

    recurring_payment = relationship("RecurringPayment")
