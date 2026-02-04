from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import AppError
from app.routes import credit_card, income, loan, recurring_payment, user

app = FastAPI()


@app.exception_handler(AppError)
async def app_error_handler(_: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "code": exc.code,
            "details": exc.details,
        },
    )


app.include_router(user.router)
app.include_router(income.router)
app.include_router(loan.router)
app.include_router(recurring_payment.router)
app.include_router(credit_card.router)
