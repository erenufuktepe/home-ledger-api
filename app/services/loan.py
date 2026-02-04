from sqlalchemy.exc import IntegrityError

from app.exceptions import NotFoundError
from app.models import Loan
from app.repositories import LoanRepository
from app.schemas import LoanCreateRequest, LoanDTO, LoanUpdateRequest
from app.utilities import ModelMapper


class LoanService:
    def __init__(self, repository: LoanRepository):
        self.repository = repository

    def get_all_loans(self) -> list[LoanDTO]:
        loans = self.repository.get_all()
        if not loans:
            return []
        return ModelMapper.from_model_list(loans, LoanDTO)

    def get_loan_by_id(self, id: int) -> LoanDTO:
        loan = self.repository.get_by_id(id)
        if not loan:
            raise NotFoundError(f"Loan with {id} id not found.")
        return ModelMapper.from_model(loan, LoanDTO)

    def create_loan(self, request: LoanCreateRequest) -> bool:
        try:
            loan = ModelMapper.from_schema(request, Loan)
            if not self.repository.insert(loan):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.payer_user_id} not found.")

    def update_loan(self, request: LoanUpdateRequest) -> bool:
        try:
            loan = self.repository.get_by_id(request.id)
            if not loan:
                raise NotFoundError(f"Loan with {id} id not found.")

            loan.payer_user_id = request.payer_user_id
            loan.name = request.name
            loan.monthly_payment = request.monthly_payment
            loan.due_day = request.due_day
            loan.end_date = request.end_date

            if not self.repository.upsert(loan):
                return False
            return True
        except IntegrityError as exc:
            raise NotFoundError(f"User with {request.payer_user_id} not found.")

    def delete_loan(self, id: int) -> bool:
        loan = self.repository.get_by_id(id)
        if not loan:
            raise NotFoundError(f"Loan with {id} id not found.")
        return self.repository.delete(loan)
