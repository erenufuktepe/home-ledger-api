from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_income_service
from app.schemas import IncomeDTO
from app.services import IncomeService

router = APIRouter(tags=["Income"])


@router.get("/income")
async def get_all_incomes(
    service: Annotated[IncomeService, Depends(get_income_service)],
) -> list[IncomeDTO]:
    return service.get_all_incomes()


@router.get("/income/{id}")
async def get_income(
    id: int, service: Annotated[IncomeService, Depends(get_income_service)]
) -> IncomeDTO | None:
    return service.get_income_by_id(id)


@router.post("/income")
async def create_income(
    username: str, service: Annotated[IncomeService, Depends(get_income_service)]
):
    pass


@router.put("/income")
async def update_income(
    income: IncomeDTO, service: Annotated[IncomeService, Depends(get_income_service)]
):
    service.update_income(income)
