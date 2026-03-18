from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_loan_service
from app.schemas import LoanCreateRequest, LoanDTO, LoanUpdateRequest
from app.services import LoanService

router = APIRouter(tags=["Loan"])


@router.get("/loan", status_code=200)
async def get_all_loans(
    service: Annotated[LoanService, Depends(get_loan_service)],
) -> list[LoanDTO]:
    return service.get_all_loans()


@router.get("/loan/user/{user_id}", status_code=200)
async def get_loans_by_user_id(
    user_id: int, service: Annotated[LoanService, Depends(get_loan_service)]
) -> list[LoanDTO]:
    return service.get_loans_by_user_id(user_id)


@router.get("/loan/{id}", status_code=200)
async def get_loan(
    id: int, service: Annotated[LoanService, Depends(get_loan_service)]
) -> LoanDTO:
    return service.get_loan_by_id(id)


@router.post("/loan", status_code=201)
async def create_loan(
    request: LoanCreateRequest,
    service: Annotated[LoanService, Depends(get_loan_service)],
) -> LoanDTO:
    return service.create_loan(request)


@router.put("/loan", status_code=200)
async def update_loan(
    request: LoanUpdateRequest,
    service: Annotated[LoanService, Depends(get_loan_service)],
) -> LoanDTO:
    return service.update_loan(request)


@router.delete("/loan/{id}", status_code=200)
async def delete_loan(
    id: int, service: Annotated[LoanService, Depends(get_loan_service)]
) -> bool:
    return service.delete_loan(id)
