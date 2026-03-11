from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import AccountType


class AccountDTO(BaseModel):
    id: int = Field(..., description="Primary key for the account.")
    user_id: int = Field(..., description="User id of the account owner.")
    name: str = Field(..., description="Account name.")
    account_type: AccountType = Field(..., description="Account type.")
    balance: Decimal = Field(..., description="Current account balance.", example=2450.75)
    apy: Decimal | None = Field(
        None, description="Annual percentage yield.", example=4.25
    )
    is_joint: bool = Field(..., description="Whether this is a joint account.")
    created_datetime: datetime | None = Field(
        None, description="Account created datetime."
    )
    updated_datetime: datetime | None = Field(
        None, description="Account updated datetime."
    )


class AccountCreateRequest(BaseModel):
    user_id: int = Field(..., description="User id of the account owner.")
    name: str = Field(..., description="Account name.")
    account_type: AccountType = Field(..., description="Account type.")
    balance: Decimal = Field(..., description="Current account balance.", example=2450.75)
    apy: Decimal | None = Field(
        None, description="Annual percentage yield.", example=4.25
    )
    is_joint: bool = Field(False, description="Whether this is a joint account.")


class AccountUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the account.")
    user_id: int = Field(..., description="User id of the account owner.")
    name: str = Field(..., description="Account name.")
    account_type: AccountType = Field(..., description="Account type.")
    balance: Decimal = Field(..., description="Current account balance.", example=2450.75)
    apy: Decimal | None = Field(
        None, description="Annual percentage yield.", example=4.25
    )
    is_joint: bool = Field(..., description="Whether this is a joint account.")
