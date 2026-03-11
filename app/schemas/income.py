from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import Frequency, IncomeType


class IncomeDTO(BaseModel):
    id: int = Field(..., description="Primary key for the income.")
    user_id: int = Field(..., description="User id of the income owner.")
    amount: Decimal = Field(..., description="Income amount.", example=3200)
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ...,
        description="Income frequency (monthly/semimonthly/yearly/biweekly/weekly).",
    )
    created_datetime: datetime | None = Field(
        None, description="Income information created in the system."
    )
    updated_datetime: datetime | None = Field(
        None, description="Income information last updated in the system."
    )


class IncomeCreateRequest(BaseModel):
    user_id: int = Field(..., description="User id of the income owner.")
    amount: Decimal = Field(..., ge=1, description="Income amount.", example=3200)
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ...,
        description="Income frequency (monthly/semimonthly/yearly/biweekly/weekly).",
    )


class IncomeUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the income.")
    user_id: int = Field(..., description="User id of the income owner.")
    amount: Decimal = Field(..., ge=1, description="Income amount.", example=3200)
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ...,
        description="Income frequency (monthly/semimonthly/yearly/biweekly/weekly).",
    )
