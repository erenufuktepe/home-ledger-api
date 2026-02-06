from sqlalchemy import case, func
from sqlalchemy.orm import Session

from app.enums import Frequency, PaymentPurpose, SpendingCategory
from app.models import CreditCard, Income, Loan, RecurringPayment, User


class DashboardRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_monthly_obligations(self):
        monthly_payment_expr = case(
            (
                RecurringPayment.frequency == Frequency.MONTHLY.value,
                RecurringPayment.amount,
            ),
            (
                RecurringPayment.frequency == Frequency.YEARLY.value,
                RecurringPayment.amount / 12,
            ),
            (
                RecurringPayment.frequency == Frequency.WEEKLY.value,
                RecurringPayment.amount * 52 / 12,
            ),
            (
                RecurringPayment.frequency == Frequency.BIWEEKLY.value,
                RecurringPayment.amount * 26 / 12,
            ),
            else_=0,
        ).label("amount")

        recurring_rows = self.session.query(
            RecurringPayment.name.label("name"),
            monthly_payment_expr,
            RecurringPayment.purpose.label("purpose"),
            RecurringPayment.category.label("category"),
        ).all()

        results = [
            {
                "name": row.name,
                "amount": row.amount,
                "purpose": row.purpose,
                "category": row.category,
            }
            for row in recurring_rows
        ]

        loans = self.session.query(Loan).all()
        results.extend(
            {
                "name": loan.name,
                "amount": loan.monthly_payment,
                "purpose": PaymentPurpose.NEED.value,
                "category": SpendingCategory.FINANCE.value,
            }
            for loan in loans
        )

        return results

    def get_user_summary(self):
        monthly_income_expr = case(
            (Income.frequency == Frequency.MONTHLY.value, Income.amount),
            (Income.frequency == Frequency.YEARLY.value, Income.amount / 12),
            (Income.frequency == Frequency.WEEKLY.value, Income.amount * 52 / 12),
            (Income.frequency == Frequency.BIWEEKLY.value, Income.amount * 26 / 12),
            else_=0,
        )
        income_subq = (
            self.session.query(
                Income.owner_user_id.label("user_id"),
                func.coalesce(func.sum(monthly_income_expr), 0).label("total_income"),
            )
            .group_by(Income.owner_user_id)
            .subquery()
        )

        monthly_payment_expr = case(
            (
                RecurringPayment.frequency == Frequency.MONTHLY.value,
                RecurringPayment.amount,
            ),
            (
                RecurringPayment.frequency == Frequency.YEARLY.value,
                RecurringPayment.amount / 12,
            ),
            (
                RecurringPayment.frequency == Frequency.WEEKLY.value,
                RecurringPayment.amount * 52 / 12,
            ),
            (
                RecurringPayment.frequency == Frequency.BIWEEKLY.value,
                RecurringPayment.amount * 26 / 12,
            ),
            else_=0,
        )
        recurring_expense_q = self.session.query(
            RecurringPayment.payer_user_id.label("user_id"),
            monthly_payment_expr.label("amount"),
        )
        loan_expense_q = self.session.query(
            Loan.payer_user_id.label("user_id"),
            Loan.monthly_payment.label("amount"),
        )
        expense_union = recurring_expense_q.union_all(loan_expense_q).subquery()
        expense_subq = (
            self.session.query(
                expense_union.c.user_id,
                func.coalesce(func.sum(expense_union.c.amount), 0).label(
                    "total_expenses"
                ),
            )
            .group_by(expense_union.c.user_id)
            .subquery()
        )

        credit_card_subq = (
            self.session.query(
                CreditCard.owner_user_id.label("user_id"),
                func.coalesce(func.sum(CreditCard.current_balance), 0).label(
                    "total_credit_card_balance"
                ),
            )
            .group_by(CreditCard.owner_user_id)
            .subquery()
        )

        rows = (
            self.session.query(
                User.username.label("name"),
                func.coalesce(income_subq.c.total_income, 0).label("total_income"),
                func.coalesce(expense_subq.c.total_expenses, 0).label("total_expenses"),
                func.coalesce(credit_card_subq.c.total_credit_card_balance, 0).label(
                    "total_credit_card_balance"
                ),
            )
            .outerjoin(income_subq, income_subq.c.user_id == User.id)
            .outerjoin(expense_subq, expense_subq.c.user_id == User.id)
            .outerjoin(credit_card_subq, credit_card_subq.c.user_id == User.id)
            .all()
        )

        return [
            {
                "name": row.name,
                "total_income": row.total_income,
                "total_expenses": row.total_expenses,
                "total_credit_card_balance": row.total_credit_card_balance,
            }
            for row in rows
        ]
