from sqlalchemy import (
    BigInteger,
    Column,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Income(Base):
    __tablename__ = "incomes"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    income_type = Column(String(10), nullable=False)
    frequency = Column(String(20), nullable=False)
    user = relationship("User")
