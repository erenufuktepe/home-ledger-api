from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Numeric, String, text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    name = Column(String(120), nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Numeric(12, 2), nullable=False)
    apy = Column(Numeric(5, 2), nullable=True)
    is_joint = Column(Boolean, nullable=False, server_default=text("false"))

    user = relationship("User")
