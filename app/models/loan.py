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


class Loan(Base):
    __tablename__ = "loans"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    payer_user_id = Column(BigInteger, ForeignKey("users.id"))
    monthly_payment = Column(Numeric, nullable=False)
    due_day = Column(Integer, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user = relationship("User")
