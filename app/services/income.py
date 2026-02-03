from app.models import Income
from app.repositories import IncomeRepository
from app.schemas import IncomeDTO
from app.utilities import ModelMapper


class IncomeService:
    def __init__(self, repository: IncomeRepository):
        self.repository = repository

    def get_all_incomes(self) -> list[IncomeDTO] | None:
        incomes = self.repository.get_all()
        if not incomes:
            return None
        return ModelMapper.from_model_list(incomes, IncomeDTO)

    def get_income_by_id(self, id: int) -> IncomeDTO | None:
        income = self.repository.get_by_id(id)
        if not income:
            return None
        return ModelMapper.from_model(income, IncomeDTO)

    def create_income(self, income: IncomeDTO) -> bool:
        new_income = ModelMapper.from_schema(income, Income)
        if not self.repository.insert(new_income):
            return False
        return True

    def update_income(self, income: IncomeDTO) -> bool:
        update_income = ModelMapper.from_schema(income, Income)
        if not self.repository.upsert(update_income):
            return False
        return True
