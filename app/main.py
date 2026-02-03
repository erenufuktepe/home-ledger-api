from fastapi import FastAPI

from app.routes import credit_card, income, loan, recurring_payment, user

app = FastAPI()

app.include_router(user.router)
app.include_router(income.router)
app.include_router(loan.router)
app.include_router(recurring_payment.router)
app.include_router(credit_card.router)
