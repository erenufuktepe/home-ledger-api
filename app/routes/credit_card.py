from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_credit_card_service
from app.schemas import CreditCardDTO
from app.services import CreditCardService

router = APIRouter(tags=["Credit Card"])


@router.get("/credit-card")
async def get_all_credit_cards(
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
) -> list[CreditCardDTO]:
    return service.get_all_credit_cards()


@router.get("/credit-card/{id}")
async def get_credit_card(
    id: int, service: Annotated[CreditCardService, Depends(get_credit_card_service)]
) -> CreditCardDTO | None:
    return service.get_credit_card_by_id(id)


@router.post("/credit-card")
async def create_credit_card(
    username: str,
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
):
    pass


@router.put("/credit-card")
async def update_credit_card(
    credit_card: CreditCardDTO,
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
):
    service.create_credit_card(credit_card)
