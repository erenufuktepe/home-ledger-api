from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import Frequency, PaymentPurpose, SpendingCategory
from app.schemas.user import UserDTO


class RecurringPaymentDTO(BaseModel):
    id: int = Field(..., description="Primary key for the recurring payment.")
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(..., ge=0.1, description="Recurring payment amount.")
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    created_at: datetime = Field(
        datetime.now(), description="Recurring payment created datetime in the system."
    )
    user: UserDTO = Field(..., description="User who owns the payment.")


class RecurringPaymentCreateRequest(BaseModel):
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(..., ge=0.1, description="Recurring payment amount.")
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    payer_user_id: int = Field(..., description="Payer user id.")


class RecurringPaymentUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the recurring payment.")
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(..., ge=0.1, description="Recurring payment amount.")
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    payer_user_id: int = Field(..., description="Payer user id.")
