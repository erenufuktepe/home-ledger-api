from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import Frequency, PaymentPurpose, SpendingCategory


class RecurringPaymentDTO(BaseModel):
    id: int = Field(..., description="Primary key for the recurring payment.")
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(
        ..., ge=0.1, description="Recurring payment amount.", example=89.99
    )
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    user_id: int = Field(..., description="Owner user id.")
    account_id: int | None = Field(None, description="Related account id.")
    credit_card_id: int | None = Field(None, description="Related credit card id.")
    created_datetime: datetime | None = Field(
        None, description="Recurring payment created datetime in the system."
    )
    updated_datetime: datetime | None = Field(
        None, description="Recurring payment updated datetime in the system."
    )


class RecurringPaymentCreateRequest(BaseModel):
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(
        ..., ge=0.1, description="Recurring payment amount.", example=89.99
    )
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    user_id: int = Field(..., description="Owner user id.")
    account_id: int | None = Field(None, description="Related account id.")
    credit_card_id: int | None = Field(None, description="Related credit card id.")


class RecurringPaymentUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the recurring payment.")
    name: str = Field(..., description="Recurring payment name.")
    category: SpendingCategory = Field(..., description="Recurring payment category.")
    purpose: PaymentPurpose = Field(..., description="Recurring payment pupose.")
    frequency: Frequency = Field(..., description="Recurring payment frequency.")
    amount: Decimal = Field(
        ..., ge=0.1, description="Recurring payment amount.", example=89.99
    )
    due_day: int | None = Field(
        None, ge=1, le=31, description="Recurring payment calender day."
    )
    due_month: int | None = Field(
        None, ge=1, le=12, description="Recurring payment month."
    )
    user_id: int = Field(..., description="Owner user id.")
    account_id: int | None = Field(None, description="Related account id.")
    credit_card_id: int | None = Field(None, description="Related credit card id.")
