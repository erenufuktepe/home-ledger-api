from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_cashback_rate_service
from app.schemas import (
    CashbackRateCreateRequest,
    CashbackRateDTO,
    CashbackRateUpdateRequest,
)
from app.services import CashbackRateService

router = APIRouter(tags=["Cashback Rate"])


@router.get("/cashback-rate", status_code=200)
async def get_all_cashback_rates(
    service: Annotated[CashbackRateService, Depends(get_cashback_rate_service)],
) -> list[CashbackRateDTO]:
    return service.get_all_cashback_rates()


@router.get("/cashback-rate/{id}", status_code=200)
async def get_cashback_rate(
    id: int,
    service: Annotated[CashbackRateService, Depends(get_cashback_rate_service)],
) -> CashbackRateDTO:
    return service.get_cashback_rate_by_id(id)


@router.post("/cashback-rate", status_code=201)
async def create_cashback_rate(
    request: CashbackRateCreateRequest,
    service: Annotated[CashbackRateService, Depends(get_cashback_rate_service)],
) -> bool:
    return service.create_cashback_rate(request)


@router.put("/cashback-rate", status_code=200)
async def update_cashback_rate(
    request: CashbackRateUpdateRequest,
    service: Annotated[CashbackRateService, Depends(get_cashback_rate_service)],
) -> bool:
    return service.update_cashback_rate(request)


@router.delete("/cashback-rate/{id}", status_code=200)
async def delete_cashback_rate(
    id: int,
    service: Annotated[CashbackRateService, Depends(get_cashback_rate_service)],
) -> bool:
    return service.delete_cashback_rate(id)
