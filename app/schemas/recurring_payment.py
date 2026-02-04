from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, model_validator

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

    @model_validator(mode="after")
    def validate_frequency_due_logic(self):
        if self.frequency == Frequency.MONTHLY:
            if self.due_day is None or self.due_month is not None:
                raise ValueError(
                    "For monthly frequency, due_day is required and due_month must be null."
                )
        elif self.frequency == Frequency.YEARLY:
            if self.due_day is None or self.due_month is None:
                raise ValueError(
                    "For yearly frequency, due_day and due_month are required."
                )
        elif self.frequency in (Frequency.WEEKLY, Frequency.BIWEEKLY):
            if self.due_day is not None or self.due_month is not None:
                raise ValueError(
                    "For weekly/biweekly frequency, due_day and due_month must be null."
                )
        return self


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

    @model_validator(mode="after")
    def validate_frequency_due_logic(self):
        if self.frequency == Frequency.MONTHLY:
            if self.due_day is None or self.due_month is not None:
                raise ValueError(
                    "For monthly frequency, due_day is required and due_month must be null."
                )
        elif self.frequency == Frequency.YEARLY:
            if self.due_day is None or self.due_month is None:
                raise ValueError(
                    "For yearly frequency, due_day and due_month are required."
                )
        elif self.frequency in (Frequency.WEEKLY, Frequency.BIWEEKLY):
            if self.due_day is not None or self.due_month is not None:
                raise ValueError(
                    "For weekly/biweekly frequency, due_day and due_month must be null."
                )
        return self
