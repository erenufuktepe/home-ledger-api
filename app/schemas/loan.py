from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class LoanDTO(BaseModel):
    id: int = Field(..., description="")
    name: str = Field(..., description="")
    monthly_payment: Decimal = Field(..., description="")
    due_day: int = Field(..., description="")
    end_date: date = Field(..., description="")
    user: UserDTO = Field(..., description="")
