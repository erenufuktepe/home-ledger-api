from datetime import datetime

from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
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

    def create_income(self, request: IncomeCreateRequest) -> bool:
        try:
            income = ModelMapper.from_schema(request, Income)
            income.created_at = datetime.now()
            if not self.repository.insert(income):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.owner_user_id} not found.")

    def update_income(self, request: IncomeUpdateRequest) -> bool:
        try:
            income = self.repository.get_by_id(request.id)
            if not income:
                raise NotFoundError(f"Income with {request.id} not found.")
            income.amount = request.amount
            income.income_type = request.income_type
            income.created_at = request.created_at
            income.owner_user_id = request.owner_user_id

            if not self.repository.upsert(income):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.owner_user_id} not found.")

    def delete_income(self, id: int) -> bool:
        income = self.repository.get_by_id(id)
        if not income:
            raise NotFoundError(f"Income with {id} not found.")
        return self.repository.delete(income)
