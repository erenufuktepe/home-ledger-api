from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import Income
from app.repositories import IncomeRepository
from app.schemas import IncomeCreateRequest, IncomeDTO, IncomeUpdateRequest
from app.utilities import ModelMapper


class IncomeService:
    def __init__(self, repository: IncomeRepository):
        self.repository = repository

    def get_all_incomes(self) -> list[IncomeDTO]:
        incomes = self.repository.get_all()
        if not incomes:
            return []
        return ModelMapper.from_model_list(incomes, IncomeDTO)

    def get_income_by_id(self, id: int) -> IncomeDTO:
        income = self.repository.get_by_id(id)
        if not income:
            raise NotFoundError(f"Income with {id} not found.")
        return ModelMapper.from_model(income, IncomeDTO)

    def get_incomes_by_user_id(self, user_id: int) -> list[IncomeDTO]:
        incomes = self.repository.get_all_by_user_id(user_id)
        if not incomes:
            return []
        return ModelMapper.from_model_list(incomes, IncomeDTO)

    def create_income(self, request: IncomeCreateRequest) -> IncomeDTO:
        try:
            income = ModelMapper.from_schema(request, Income)
            created = self.repository.insert(income)
            return ModelMapper.from_model(created, IncomeDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def update_income(self, request: IncomeUpdateRequest) -> IncomeDTO:
        try:
            income = self.repository.get_by_id(request.id)
            if not income:
                raise NotFoundError(f"Income with {request.id} not found.")
            income.user_id = request.user_id
            income.amount = request.amount
            income.income_type = request.income_type
            income.frequency = request.frequency

            updated = self.repository.upsert(income)
            return ModelMapper.from_model(updated, IncomeDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def delete_income(self, id: int) -> bool:
        income = self.repository.get_by_id(id)
        if not income:
            raise NotFoundError(f"Income with {id} not found.")
        return self.repository.delete(income)
