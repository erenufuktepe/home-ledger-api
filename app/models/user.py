from sqlalchemy import BigInteger, Column, String

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
