from sqlalchemy import Column, DateTime, MetaData, func
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData(schema="finance")


class Base(DeclarativeBase):
    metadata = metadata
    created_datetime = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
