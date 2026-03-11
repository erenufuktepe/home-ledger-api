from sqlalchemy import (
    BigInteger,
    Column,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from app.models.base import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    current_balance = Column(Numeric(12, 2), nullable=False)
    apr = Column(Numeric(5, 2), nullable=True)
    credit_limit = Column(Numeric(12, 2), nullable=True)
    user = relationship("User")
