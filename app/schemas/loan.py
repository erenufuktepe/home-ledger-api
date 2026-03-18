from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field

class LoanDTO(BaseModel):
    id: int = Field(..., description="Primary key for the loan.")
    user_id: int = Field(..., description="Id of the user who pays the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(
        ..., description="Monthly payment amount.", example=425
    )
    remaining_amount: Decimal = Field(
        ..., description="Remaining loan principal amount.", example=18500
    )
    apr: Decimal | None = Field(None, description="Loan APR percentage.", example=6.75)
    due_day: int = Field(..., description="Due day for the paymet (1-31).")
    end_date: date | None = Field(None, description="Last payment date for the loan.")
    created_datetime: datetime | None = Field(None, description="Record creation timestamp.")
    updated_datetime: datetime | None = Field(None, description="Record last updated timestamp.")


class LoanCreateRequest(BaseModel):
    user_id: int = Field(..., description="Id of the user who pays the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(
        ..., ge=1, description="Monthly payment amount.", example=425
    )
    remaining_amount: Decimal = Field(
        ..., ge=0, description="Remaining loan principal amount.", example=18500
    )
    apr: Decimal | None = Field(None, description="Loan APR percentage.", example=6.75)
    due_day: int = Field(..., ge=1, le=31, description="Due day for the paymet (1-31).")
    end_date: date | None = Field(None, description="Last payment date for the loan.")


class LoanUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the loan.")
    user_id: int = Field(..., description="Id of the user who pays the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(
        ..., description="Monthly payment amount.", example=425
    )
    remaining_amount: Decimal = Field(
        ..., ge=0, description="Remaining loan principal amount.", example=18500
    )
    apr: Decimal | None = Field(None, description="Loan APR percentage.", example=6.75)
    due_day: int = Field(..., description="Due day for the paymet (1-31).")
    end_date: date | None = Field(None, description="Last payment date for the loan.")
