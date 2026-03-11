from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class TransactionDTO(BaseModel):
    id: int = Field(..., description="Primary key for the transaction.")
    amount: Decimal = Field(..., description="Transaction amount.", example=64.99)
    recurring_payment_id: int | None = Field(
        None, description="Related recurring payment id."
    )
    transaction_datetime: datetime = Field(..., description="Transaction datetime.")
    created_datetime: datetime | None = Field(
        None, description="Transaction created datetime."
    )
    updated_datetime: datetime | None = Field(
        None, description="Transaction updated datetime."
    )


class TransactionCreateRequest(BaseModel):
    amount: Decimal = Field(..., description="Transaction amount.", example=64.99)
    recurring_payment_id: int | None = Field(
        None, description="Related recurring payment id."
    )
    transaction_datetime: datetime = Field(..., description="Transaction datetime.")


class TransactionUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the transaction.")
    amount: Decimal = Field(..., description="Transaction amount.", example=64.99)
    recurring_payment_id: int | None = Field(
        None, description="Related recurring payment id."
    )
    transaction_datetime: datetime = Field(..., description="Transaction datetime.")
