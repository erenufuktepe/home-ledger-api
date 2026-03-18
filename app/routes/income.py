from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_income_service
from app.schemas import IncomeCreateRequest, IncomeDTO, IncomeUpdateRequest
from app.services import IncomeService

router = APIRouter(tags=["Income"])


@router.get("/income", status_code=200)
async def get_all_incomes(
    service: Annotated[IncomeService, Depends(get_income_service)],
) -> list[IncomeDTO]:
    return service.get_all_incomes()


@router.get("/income/user/{user_id}", status_code=200)
async def get_incomes_by_user_id(
    user_id: int, service: Annotated[IncomeService, Depends(get_income_service)]
) -> list[IncomeDTO]:
    return service.get_incomes_by_user_id(user_id)


@router.get("/income/{id}", status_code=200)
async def get_income(
    id: int, service: Annotated[IncomeService, Depends(get_income_service)]
) -> IncomeDTO:
    return service.get_income_by_id(id)


@router.post("/income", status_code=201)
async def create_income(
    request: IncomeCreateRequest,
    service: Annotated[IncomeService, Depends(get_income_service)],
) -> IncomeDTO:
    return service.create_income(request)


@router.put("/income", status_code=200)
async def update_income(
    request: IncomeUpdateRequest,
    service: Annotated[IncomeService, Depends(get_income_service)],
) -> IncomeDTO:
    return service.update_income(request)


@router.delete("/income/{id}", status_code=200)
async def delete_income(
    id: int, service: Annotated[IncomeService, Depends(get_income_service)]
) -> bool:
    return service.delete_income(id)
