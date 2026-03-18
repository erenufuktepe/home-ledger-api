from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
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

    def get_loans_by_user_id(self, user_id: int) -> list[LoanDTO]:
        loans = self.repository.get_all_by_user_id(user_id)
        if not loans:
            return []
        return ModelMapper.from_model_list(loans, LoanDTO)

    def create_loan(self, request: LoanCreateRequest) -> LoanDTO:
        try:
            loan = ModelMapper.from_schema(request, Loan)
            created = self.repository.insert(loan)
            return ModelMapper.from_model(created, LoanDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def update_loan(self, request: LoanUpdateRequest) -> LoanDTO:
        try:
            loan = self.repository.get_by_id(request.id)
            if not loan:
                raise NotFoundError(f"Loan with {request.id} id not found.")

            loan.user_id = request.user_id
            loan.name = request.name
            loan.monthly_payment = request.monthly_payment
            loan.remaining_amount = request.remaining_amount
            loan.apr = request.apr
            loan.due_day = request.due_day
            loan.end_date = request.end_date

            updated = self.repository.upsert(loan)
            return ModelMapper.from_model(updated, LoanDTO)
        except IntegrityError as exc:
            raise ConflictError({"user_id": request.user_id}, message=f"User with id {request.user_id} not found.") from exc

    def delete_loan(self, id: int) -> bool:
        loan = self.repository.get_by_id(id)
        if not loan:
            raise NotFoundError(f"Loan with {id} id not found.")
        return self.repository.delete(loan)
