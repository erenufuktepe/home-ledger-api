from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_recurring_payment_service
from app.schemas import RecurringPaymentDTO
from app.services import RecurringPaymentService

router = APIRouter(tags=["Recurring Payment"])


@router.get("/recurring-payment")
async def get_all_recurring_payments(
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> list[RecurringPaymentDTO]:
    return service.get_all_recurring_payments()


@router.get("/recurring-payment/{id}")
async def get_recurring_payment(
    id: int,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
) -> RecurringPaymentDTO | None:
    return service.get_recurring_payment_by_id(id)


@router.post("/recurring-payment")
async def create_recurring_payment(
    recurring_paymentname: str,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
):
    pass


@router.put("/recurring-payment")
async def update_recurring_payment(
    recurring_payments: RecurringPaymentDTO,
    service: Annotated[RecurringPaymentService, Depends(get_recurring_payment_service)],
):
    service.update_recurring_payment(recurring_payments)
