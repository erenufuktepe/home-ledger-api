from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories import (
    CreditCardRepository,
    IncomeRepository,
    LoanRepository,
    RecurringPaymentRepository,
    UserRepository,
)
from app.services import (
    CreditCardService,
    IncomeService,
    LoanService,
    RecurringPaymentService,
    UserService,
)


def get_user_service(db: Session = Depends(get_session)) -> UserService:
    return UserService(UserRepository(db))


def get_credit_card_service(db: Session = Depends(get_session)) -> CreditCardService:
    return CreditCardService(CreditCardRepository(db))


def get_loan_service(db: Session = Depends(get_session)) -> LoanService:
    return LoanService(LoanRepository(db))


def get_income_service(db: Session = Depends(get_session)) -> IncomeService:
    return IncomeService(IncomeRepository(db))


def get_recurring_payment_service(
    db: Session = Depends(get_session),
) -> RecurringPaymentService:
    return RecurringPaymentService(RecurringPaymentRepository(db))
