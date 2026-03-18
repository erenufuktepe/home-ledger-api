from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.exceptions import AppError
from app.routes import (
    account,
    credit_card,
    dashboard,
    income,
    loan,
    metadata,
    recurring_payment,
    user,
)
from app.settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "code": "internal_error", "details": None},
    )


app.include_router(dashboard.router)
app.include_router(user.router)
app.include_router(account.router)
app.include_router(income.router)
app.include_router(loan.router)
app.include_router(credit_card.router)
app.include_router(recurring_payment.router)
app.include_router(metadata.router)
