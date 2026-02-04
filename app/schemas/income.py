from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import Frequency, IncomeType
from app.schemas.user import UserDTO


class IncomeDTO(BaseModel):
    id: int = Field(..., description="Primary key for the income.")
    amount: Decimal = Field(..., description="Income amount.")
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ..., description="Income frequency (monthly/yearly/biweekly/weekly)."
    )
    created_at: datetime = Field(
        datetime.now(), description="Income information created in the system."
    )
    user: UserDTO = Field(..., description="Income owner.")


class IncomeCreateRequest(BaseModel):
    amount: Decimal = Field(..., ge=1, description="Income amount.")
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ..., description="Income frequency (monthly/yearly/biweekly/weekly)."
    )
    created_at: datetime = Field(
        datetime.now(), description="Income information created in the system."
    )
    owner_user_id: int = Field(..., description="User id of the income owner.")


class IncomeUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the income.")
    amount: Decimal = Field(..., ge=1, description="Income amount.")
    income_type: IncomeType = Field(..., description="Income type (primary/secondary).")
    frequency: Frequency = Field(
        ..., description="Income frequency (monthly/yearly/biweekly/weekly)."
    )

    created_at: datetime = Field(
        datetime.now(), description="Income information created in the system."
    )
    owner_user_id: int = Field(..., description="User id of the income owner.")
