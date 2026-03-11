from sqlalchemy import (
    BigInteger,
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(150), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    monthly_payment = Column(Numeric(12, 2), nullable=False)
    remaining_amount = Column(Numeric(12, 2), nullable=False)
    apr = Column(Numeric(5, 2), nullable=True)
    due_day = Column(Integer, nullable=False)
    end_date = Column(Date, nullable=True)
    user = relationship("User")
