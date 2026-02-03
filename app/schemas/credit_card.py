from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class CreditCardDTO(BaseModel):
    id: int = Field(..., description="")
    name: str = Field(..., description="")
    current_balance: Decimal = Field(..., description="")
    user: UserDTO = Field(..., description="")
