from sqlalchemy import BigInteger, Column, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.models.base import Base


class CashbackRate(Base):
    __tablename__ = "cashback_rates"
    __table_args__ = (
        UniqueConstraint(
            "card_id", "category", name="uq_cashback_rates_card_category"
        ),
    )

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    card_id = Column(BigInteger, ForeignKey("credit_cards.id"), nullable=False)
    category = Column(String(50), nullable=False)
    percentage = Column(Numeric(5, 2), nullable=False)

    card = relationship("CreditCard")
