from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import User
from app.repositories import UserRepository
from app.schemas import UserCreateRequest, UserDTO, UserUpdateRequest
from app.utilities import ModelMapper


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self) -> list[UserDTO]:
        users = self.repository.get_all()
        if not users:
            return []
        return ModelMapper.from_model_list(users, UserDTO)

    def get_user_by_id(self, id: int) -> UserDTO:
        user = self.repository.get_by_id(id)
        if not user:
            raise NotFoundError(f"User with {id} id not found.")
        return ModelMapper.from_model(user, UserDTO)

    def create_user(self, request: UserCreateRequest) -> UserDTO:
        try:
            user = ModelMapper.from_schema(request, User)
            created = self.repository.insert(user)
            return ModelMapper.from_model(created, UserDTO)
        except IntegrityError as exc:
            raise ConflictError({"username": request.username}, message=f"User {request.username.title()} already exists.") from exc

    def update_user(self, request: UserUpdateRequest) -> UserDTO:
        user = self.repository.get_by_id(request.id)

        if not user:
            raise NotFoundError(f"User with {request.id} id not found.")
        user.username = request.username.title()
        updated = self.repository.upsert(user)
        return ModelMapper.from_model(updated, UserDTO)

    def delete_user(self, id: int) -> bool:
        user = self.repository.get_by_id(id)
        if not user:
            raise NotFoundError(f"User with {id} id not found.")
        return self.repository.delete(user)
