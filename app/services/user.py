from sqlalchemy.exc import IntegrityError

from app.exceptions import UserExistsError, UserNotFoundError
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
            raise UserNotFoundError(id)
        return ModelMapper.from_model(user, UserDTO)

    def create_user(self, request: UserCreateRequest) -> bool:
        try:
            user = UserDTO(username=request.username.title())
            new_user = ModelMapper.from_schema(user, User)
            if not self.repository.insert(new_user):
                return False
            return True
        except IntegrityError as exc:
            raise UserExistsError(request.username)

    def update_user(self, request: UserUpdateRequest) -> bool:
        user = self.repository.get_by_id(request.id)

        if not user:
            raise UserNotFoundError(request.id)
        user.username = request.username.title()
        if not self.repository.upsert(user):
            return False
        return True

    def delete_user(self, id: int) -> bool:
        user = self.repository.get_by_id(id)
        if not user:
            raise UserNotFoundError(id)
        if not self.repository.delete(user):
            return False
        return True
