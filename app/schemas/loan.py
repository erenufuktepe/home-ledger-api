from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class LoanDTO(BaseModel):
    id: int = Field(..., description="Primary key for the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(..., description="Monthly payment amount.")
    due_day: int = Field(..., description="Due day for the paymet (1-31).")
    end_date: date = Field(..., description="Last payment for the loan.")
    user: UserDTO = Field(..., description="User who pays the loan")


class LoanCreateRequest(BaseModel):
    payer_user_id: int = Field(..., description="Id of the user who pays the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(..., ge=1, description="Monthly payment amount.")
    due_day: int = Field(..., ge=1, le=31, description="Due day for the paymet (1-31).")
    end_date: date = Field(..., description="Last payment for the loan.")


class LoanUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the loan.")
    payer_user_id: int = Field(..., description="Id of the user who pays the loan.")
    name: str = Field(..., description="Name of the loan.")
    monthly_payment: Decimal = Field(..., description="Monthly payment amount.")
    due_day: int = Field(..., description="Due day for the paymet (1-31).")
    end_date: date = Field(..., description="Last payment for the loan.")
