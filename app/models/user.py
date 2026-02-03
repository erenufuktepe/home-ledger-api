from sqlalchemy import BigInteger, Column, DateTime, String

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
