from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class RecurringPaymentDTO(BaseModel):
    id: int = Field(..., description="")
    name: str = Field(..., description="")
    category: str = Field(..., description="")
    purpose: str = Field(..., description="")
    frequency: int = Field(..., description="")
    amount: Decimal = Field(..., description="")
    due_day: int = Field(..., description="")
    due_month: int = Field(..., description="")
    created_at: datetime = Field(..., description="")
    user: UserDTO = Field(..., description="")
