from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_user_service
from app.schemas import UserCreateRequest, UserDTO, UserUpdateRequest
from app.services import UserService

router = APIRouter(tags=["User"])


@router.get("/user", status_code=200)
async def get_all_users(
    service: Annotated[UserService, Depends(get_user_service)],
) -> list[UserDTO]:
    return service.get_all_users()


@router.get("/user/{id}", status_code=200)
async def get_user(
    id: int, service: Annotated[UserService, Depends(get_user_service)]
) -> UserDTO:
    return service.get_user_by_id(id)


@router.post("/user", status_code=201)
async def create_user(
    request: UserCreateRequest,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserDTO:
    return service.create_user(request)


@router.put("/user", status_code=200)
async def update_user(
    request: UserUpdateRequest,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserDTO:
    return service.update_user(request)


@router.delete("/user/{id}", status_code=200)
async def delete_user(
    id: int, service: Annotated[UserService, Depends(get_user_service)]
) -> bool:
    return service.delete_user(id)
