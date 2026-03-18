from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_account_service
from app.schemas import AccountCreateRequest, AccountDTO, AccountUpdateRequest
from app.services import AccountService

router = APIRouter(tags=["Account"])


@router.get("/account", status_code=200)
async def get_all_accounts(
    service: Annotated[AccountService, Depends(get_account_service)],
) -> list[AccountDTO]:
    return service.get_all_accounts()


@router.get("/account/user/{user_id}", status_code=200)
async def get_accounts_by_user_id(
    user_id: int, service: Annotated[AccountService, Depends(get_account_service)]
) -> list[AccountDTO]:
    return service.get_accounts_by_user_id(user_id)


@router.get("/account/{id}", status_code=200)
async def get_account(
    id: int, service: Annotated[AccountService, Depends(get_account_service)]
) -> AccountDTO:
    return service.get_account_by_id(id)


@router.post("/account", status_code=201)
async def create_account(
    request: AccountCreateRequest,
    service: Annotated[AccountService, Depends(get_account_service)],
) -> AccountDTO:
    return service.create_account(request)


@router.put("/account", status_code=200)
async def update_account(
    request: AccountUpdateRequest,
    service: Annotated[AccountService, Depends(get_account_service)],
) -> AccountDTO:
    return service.update_account(request)


@router.delete("/account/{id}", status_code=200)
async def delete_account(
    id: int, service: Annotated[AccountService, Depends(get_account_service)]
) -> bool:
    return service.delete_account(id)
