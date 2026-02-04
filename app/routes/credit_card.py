from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_credit_card_service
from app.schemas import CreditCardCreateRequest, CreditCardDTO, CreditCardUpdateRequest
from app.services import CreditCardService

router = APIRouter(tags=["Credit Card"])


@router.get("/credit-card", status_code=200)
async def get_all_credit_cards(
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
) -> list[CreditCardDTO]:
    return service.get_all_credit_cards()


@router.get("/credit-card/{id}", status_code=200)
async def get_credit_card(
    id: int, service: Annotated[CreditCardService, Depends(get_credit_card_service)]
) -> CreditCardDTO:
    return service.get_credit_card_by_id(id)


@router.post("/credit-card", status_code=201)
async def create_credit_card(
    request: CreditCardCreateRequest,
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
) -> bool:
    return service.create_credit_card(request)


@router.put("/credit-card", status_code=200)
async def update_credit_card(
    request: CreditCardUpdateRequest,
    service: Annotated[CreditCardService, Depends(get_credit_card_service)],
) -> bool:
    return service.update_credit_card(request)


@router.delete("/credit-card/{id}", status_code=200)
async def delete_credit_card(
    id: int, service: Annotated[CreditCardService, Depends(get_credit_card_service)]
) -> bool:
    return service.delete_credit_card(id)
