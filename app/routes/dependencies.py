from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories import (
    AccountRepository,
    AccountSnapshotRepository,
    CashbackRateRepository,
    CreditCardRepository,
    DashboardRepository,
    IncomeRepository,
    LoanRepository,
    RecurringPaymentRepository,
    TransactionRepository,
    UserRepository,
)
from app.services import (
    AccountService,
    AccountSnapshotService,
    CashbackRateService,
    CreditCardService,
    DashboardService,
    IncomeService,
    LoanService,
    RecurringPaymentService,
    TransactionService,
    UserService,
)


def get_user_service(db: Session = Depends(get_session)) -> UserService:
    return UserService(UserRepository(db))


def get_credit_card_service(db: Session = Depends(get_session)) -> CreditCardService:
    return CreditCardService(CreditCardRepository(db))


def get_cashback_rate_service(
    db: Session = Depends(get_session),
) -> CashbackRateService:
    return CashbackRateService(CashbackRateRepository(db))


def get_loan_service(db: Session = Depends(get_session)) -> LoanService:
    return LoanService(LoanRepository(db))


def get_income_service(db: Session = Depends(get_session)) -> IncomeService:
    return IncomeService(IncomeRepository(db))


def get_account_service(db: Session = Depends(get_session)) -> AccountService:
    return AccountService(AccountRepository(db), AccountSnapshotRepository(db))


def get_account_snapshot_service(
    db: Session = Depends(get_session),
) -> AccountSnapshotService:
    return AccountSnapshotService(AccountSnapshotRepository(db))


def get_transaction_service(db: Session = Depends(get_session)) -> TransactionService:
    return TransactionService(TransactionRepository(db))


def get_recurring_payment_service(
    db: Session = Depends(get_session),
) -> RecurringPaymentService:
    return RecurringPaymentService(RecurringPaymentRepository(db))


def get_dashboard_service(
    db: Session = Depends(get_session),
) -> DashboardService:
    return DashboardService(DashboardRepository(db))
