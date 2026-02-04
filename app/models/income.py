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


class Income(Base):
    __tablename__ = "incomes"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    owner_user_id = Column(BigInteger, ForeignKey("users.id"))
    amount = Column(Numeric, nullable=False)
    income_type = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    created_at = Column(DateTime)
    user = relationship("User")
