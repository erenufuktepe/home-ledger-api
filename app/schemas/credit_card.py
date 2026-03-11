from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field

class CreditCardDTO(BaseModel):
    id: int = Field(..., description="Primary key for the credit card.")
    user_id: int = Field(..., description="User id of the credit card owner.")
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(
        ..., description="Current balance of the credit card.", example=380.5
    )
    apr: Decimal | None = Field(None, description="Card APR percentage.", example=19.99)
    credit_limit: Decimal | None = Field(
        None, description="Card credit limit.", example=5000
    )
    created_datetime: datetime | None = Field(
        None, description="Credit card created datetime."
    )
    updated_datetime: datetime | None = Field(
        None, description="Credit card updated datetime."
    )


class CreditCardCreateRequest(BaseModel):
    user_id: int = Field(..., description="User id of the credit card owner.")
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(
        ..., description="Current balance of credit card.", example=380.5
    )
    apr: Decimal | None = Field(None, description="Card APR percentage.", example=19.99)
    credit_limit: Decimal | None = Field(
        None, description="Card credit limit.", example=5000
    )


class CreditCardUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the credit card.")
    user_id: int = Field(..., description="User id of the credit card owner.")
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(
        ..., description="Current balance of the credit card.", example=380.5
    )
    apr: Decimal | None = Field(None, description="Card APR percentage.", example=19.99)
    credit_limit: Decimal | None = Field(
        None, description="Card credit limit.", example=5000
    )
