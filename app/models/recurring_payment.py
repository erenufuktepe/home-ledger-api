from sqlalchemy import (
    BigInteger,
    Column,
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
    name = Column(String(150), nullable=False)
    category = Column(String(50), nullable=False)
    purpose = Column(String(10), nullable=False)
    frequency = Column(String(20), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    due_day = Column(Integer, nullable=True)
    due_month = Column(Integer, nullable=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=True)
    credit_card_id = Column(BigInteger, ForeignKey("credit_cards.id"), nullable=True)
    user = relationship("User")
    account = relationship("Account")
    credit_card = relationship("CreditCard")
