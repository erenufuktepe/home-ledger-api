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


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    owner_user_id = Column(BigInteger, ForeignKey("users.id"))
    current_balance = Column(Numeric, nullable=False)
    user = relationship("User")
