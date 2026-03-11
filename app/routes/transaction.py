from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_transaction_service
from app.schemas import (
    TransactionCreateRequest,
    TransactionDTO,
    TransactionUpdateRequest,
)
from app.services import TransactionService

router = APIRouter(tags=["Transaction"])


@router.get("/transaction", status_code=200)
async def get_all_transactions(
    service: Annotated[TransactionService, Depends(get_transaction_service)],
) -> list[TransactionDTO]:
    return service.get_all_transactions()


@router.get("/transaction/{id}", status_code=200)
async def get_transaction(
    id: int, service: Annotated[TransactionService, Depends(get_transaction_service)]
) -> TransactionDTO:
    return service.get_transaction_by_id(id)


@router.post("/transaction", status_code=201)
async def create_transaction(
    request: TransactionCreateRequest,
    service: Annotated[TransactionService, Depends(get_transaction_service)],
) -> bool:
    return service.create_transaction(request)


@router.put("/transaction", status_code=200)
async def update_transaction(
    request: TransactionUpdateRequest,
    service: Annotated[TransactionService, Depends(get_transaction_service)],
) -> bool:
    return service.update_transaction(request)


@router.delete("/transaction/{id}", status_code=200)
async def delete_transaction(
    id: int, service: Annotated[TransactionService, Depends(get_transaction_service)]
) -> bool:
    return service.delete_transaction(id)
