from datetime import datetime

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

    def create_user(self, request: UserCreateRequest) -> bool:
        try:
            user = ModelMapper.from_schema(request, User)
            user.created_at = datetime.now()
            if not self.repository.insert(user):
                return False
            return True
        except IntegrityError as exc:
            raise ConflictError(f"User {request.username.title()} already exists.")

    def update_user(self, request: UserUpdateRequest) -> bool:
        user = self.repository.get_by_id(request.id)

        if not user:
            raise NotFoundError(f"User with {request.id} id not found.")
        user.username = request.username.title()
        if not self.repository.upsert(user):
            return False
        return True

    def delete_user(self, id: int) -> bool:
        user = self.repository.get_by_id(id)
        if not user:
            raise NotFoundError(f"User with {id} id not found.")
        return self.repository.delete(user)
