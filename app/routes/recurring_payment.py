from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_recurring_payment_service
from app.schemas import (
    RecurringPaymentCreateRequest,
    RecurringPaymentDTO,
    RecurringPaymentUpdateRequest,
)
from app.services import RecurringPaymentService

router = APIRouter(tags=["Recurring Payment"])


@router.get("/recurring-payment", status_code=200)
async def get_all_recurring_payments(
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> list[RecurringPaymentDTO]:
    return service.get_all_recurring_payments()


@router.get("/recurring-payment/user/{user_id}", status_code=200)
async def get_recurring_payments_by_user_id(
    user_id: int,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> list[RecurringPaymentDTO]:
    return service.get_recurring_payments_by_user_id(user_id)


@router.get("/recurring-payment/{id}", status_code=200)
async def get_recurring_payment(
    id: int,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> RecurringPaymentDTO:
    return service.get_recurring_payment_by_id(id)


@router.post("/recurring-payment", status_code=201)
async def create_recurring_payment(
    request: RecurringPaymentCreateRequest,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> RecurringPaymentDTO:
    return service.create_recurring_payment(request)


@router.put("/recurring-payment", status_code=200)
async def update_recurring_payment(
    request: RecurringPaymentUpdateRequest,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> RecurringPaymentDTO:
    return service.update_recurring_payment(request)


@router.delete("/recurring-payment/{id}", status_code=200)
async def delete_recurring_payment(
    id: int,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> bool:
    return service.delete_recurring_payment(id)
