from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData(schema="finance")


class Base(DeclarativeBase):
    metadata = metadata
