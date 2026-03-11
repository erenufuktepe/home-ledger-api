from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.models.base import Base


class AccountSnapshot(Base):
    __tablename__ = "account_snapshots"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=False)
    balance = Column(Numeric(12, 2), nullable=False)
    snapshot_datetime = Column(DateTime, nullable=False)

    account = relationship("Account")
