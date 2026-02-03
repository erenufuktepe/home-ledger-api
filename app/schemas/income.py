from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class IncomeDTO(BaseModel):
    id: int = Field(..., description="")
    amount: Decimal = Field(..., description="")
    income_type: str = Field(..., description="")
    created_at: datetime = Field(..., description="")
    user: UserDTO = Field(..., description="")
