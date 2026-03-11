from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_account_snapshot_service
from app.schemas import (
    AccountSnapshotCreateRequest,
    AccountSnapshotDTO,
    AccountSnapshotUpdateRequest,
)
from app.services import AccountSnapshotService

router = APIRouter(tags=["Account Snapshot"])


@router.get("/account-snapshot", status_code=200)
async def get_all_account_snapshots(
    service: Annotated[AccountSnapshotService, Depends(get_account_snapshot_service)],
) -> list[AccountSnapshotDTO]:
    return service.get_all_account_snapshots()


@router.get("/account-snapshot/{id}", status_code=200)
async def get_account_snapshot(
    id: int,
    service: Annotated[AccountSnapshotService, Depends(get_account_snapshot_service)],
) -> AccountSnapshotDTO:
    return service.get_account_snapshot_by_id(id)


@router.post("/account-snapshot", status_code=201)
async def create_account_snapshot(
    request: AccountSnapshotCreateRequest,
    service: Annotated[AccountSnapshotService, Depends(get_account_snapshot_service)],
) -> bool:
    return service.create_account_snapshot(request)


@router.put("/account-snapshot", status_code=200)
async def update_account_snapshot(
    request: AccountSnapshotUpdateRequest,
    service: Annotated[AccountSnapshotService, Depends(get_account_snapshot_service)],
) -> bool:
    return service.update_account_snapshot(request)


@router.delete("/account-snapshot/{id}", status_code=200)
async def delete_account_snapshot(
    id: int,
    service: Annotated[AccountSnapshotService, Depends(get_account_snapshot_service)],
) -> bool:
    return service.delete_account_snapshot(id)
