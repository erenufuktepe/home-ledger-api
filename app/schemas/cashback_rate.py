from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import SpendingCategory


class CashbackRateDTO(BaseModel):
    id: int = Field(..., description="Primary key for the cashback rate.")
    card_id: int = Field(..., description="Related credit card id.")
    category: SpendingCategory = Field(..., description="Spending category.")
    percentage: Decimal = Field(..., description="Cashback percentage.", example=2.0)
    created_datetime: datetime | None = Field(
        None, description="Cashback rate created datetime."
    )
    updated_datetime: datetime | None = Field(
        None, description="Cashback rate updated datetime."
    )


class CashbackRateCreateRequest(BaseModel):
    card_id: int = Field(..., description="Related credit card id.")
    category: SpendingCategory = Field(..., description="Spending category.")
    percentage: Decimal = Field(..., description="Cashback percentage.", example=2.0)


class CashbackRateUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the cashback rate.")
    card_id: int = Field(..., description="Related credit card id.")
    category: SpendingCategory = Field(..., description="Spending category.")
    percentage: Decimal = Field(..., description="Cashback percentage.", example=2.0)
