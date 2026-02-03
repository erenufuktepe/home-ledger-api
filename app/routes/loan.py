from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_loan_service
from app.schemas import LoanDTO
from app.services import LoanService

router = APIRouter(tags=["Loan"])


@router.get("/loan")
async def get_all_loans(
    service: Annotated[LoanService, Depends(get_loan_service)],
) -> list[LoanDTO]:
    return service.get_all_loans()


@router.get("/loan/{id}")
async def get_loan(
    id: int, service: Annotated[LoanService, Depends(get_loan_service)]
) -> LoanDTO | None:
    return service.get_loan_by_id(id)


@router.post("/loan")
async def create_loan(
    loanname: str, service: Annotated[LoanService, Depends(get_loan_service)]
):
    pass


@router.put("/loan")
async def update_loan(
    loan: LoanDTO, service: Annotated[LoanService, Depends(get_loan_service)]
):
    service.update_loan(loan)
