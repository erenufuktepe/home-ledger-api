from app.models import Loan
from app.repositories import LoanRepository
from app.schemas import LoanDTO
from app.utilities import ModelMapper


class LoanService:
    def __init__(self, repository: LoanRepository):
        self.repository = repository

    def get_all_loans(self) -> list[LoanDTO] | None:
        loans = self.repository.get_all()
        if not loans:
            return None
        return ModelMapper.from_model_list(loans, LoanDTO)

    def get_loan_by_id(self, id: int) -> LoanDTO | None:
        loan = self.repository.get_by_id(id)
        if not loan:
            return None
        return ModelMapper.from_model(loan, LoanDTO)

    def create_loan(self, loan: LoanDTO) -> bool:
        new_loan = ModelMapper.from_schema(loan, Loan)
        if not self.repository.insert(new_loan):
            return False
        return True

    def update_loan(self, loan: LoanDTO) -> bool:
        update_loan = ModelMapper.from_schema(loan, Loan)
        if not self.repository.upsert(update_loan):
            return False
        return True
