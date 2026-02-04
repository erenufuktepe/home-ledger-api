from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.user import UserDTO


class CreditCardDTO(BaseModel):
    id: int = Field(..., description="Primary key for the credit card.")
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(
        ..., description="Current balance of the credit card."
    )
    user: UserDTO = Field(..., description="Credit card owner.")


class CreditCardCreateRequest(BaseModel):
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(..., description="Current balance of credit card.")
    owner_user_id: int = Field(..., description="User id of the credit card owner.")


class CreditCardUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the credit card.")
    name: str = Field(..., description="Name of the credit card.")
    current_balance: Decimal = Field(
        ..., description="Current balance of the credit card."
    )
