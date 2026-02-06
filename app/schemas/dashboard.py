from decimal import Decimal

from pydantic import BaseModel, Field

from app.enums import PaymentPurpose, SpendingCategory


class Payment(BaseModel):
    name: str = Field(..., description="Name of the payment.")
    amount: Decimal = Field(..., description="Monthly amount paid.")
    purpose: PaymentPurpose = Field(..., description="Payment purpose.")
    category: SpendingCategory = Field(..., description="Spending category.")


class User(BaseModel):
    name: str = Field(..., description="Username")
    total_income: Decimal = Field(
        ..., description="Monthly total income for the person."
    )
    total_expenses: Decimal = Field(
        ..., description="Monthly total expenses for the person."
    )
    total_credit_card_balance: Decimal = Field(
        ..., description="Total credit card balances."
    )


class Dashboard(BaseModel):
    users: list[User] = Field(..., description="User sumary information.")
    payments: list[Payment] = Field(..., description="Monthly payments.")
