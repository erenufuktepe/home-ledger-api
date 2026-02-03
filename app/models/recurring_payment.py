from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from app.models.base import Base


class RecurringPayment(Base):
    __tablename__ = "recurring_payments"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    purpose = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    due_day = Column(Integer, nullable=True)
    due_month = Column(Integer, nullable=True)
    payer_user_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(DateTime, nullable=False)
    user = relationship("User")
