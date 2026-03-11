from sqlalchemy.exc import IntegrityError

from app.exceptions import ConflictError, NotFoundError
from app.models import CashbackRate
from app.repositories import CashbackRateRepository
from app.schemas import (
    CashbackRateCreateRequest,
    CashbackRateDTO,
    CashbackRateUpdateRequest,
)
from app.utilities import ModelMapper


class CashbackRateService:
    def __init__(self, repository: CashbackRateRepository):
        self.repository = repository

    def get_all_cashback_rates(self) -> list[CashbackRateDTO]:
        rates = self.repository.get_all()
        if not rates:
            return []
        return ModelMapper.from_model_list(rates, CashbackRateDTO)

    def get_cashback_rate_by_id(self, id: int) -> CashbackRateDTO:
        rate = self.repository.get_by_id(id)
        if not rate:
            raise NotFoundError(f"Cashback rate with {id} id not found.")
        return ModelMapper.from_model(rate, CashbackRateDTO)

    def create_cashback_rate(self, request: CashbackRateCreateRequest) -> bool:
        try:
            rate = ModelMapper.from_schema(request, CashbackRate)
            if not self.repository.insert(rate):
                return False
            return True
        except IntegrityError as exc:
            raise ConflictError(
                f"Cashback rate for card {request.card_id} and {request.category} exists."
            )

    def update_cashback_rate(self, request: CashbackRateUpdateRequest) -> bool:
        try:
            rate = self.repository.get_by_id(request.id)
            if not rate:
                raise NotFoundError(f"Cashback rate with {request.id} id not found.")

            rate.card_id = request.card_id
            rate.category = request.category
            rate.percentage = request.percentage

            if not self.repository.upsert(rate):
                return False
            return True
        except IntegrityError as exc:
            raise ConflictError(
                f"Cashback rate for card {request.card_id} and {request.category} exists."
            )

    def delete_cashback_rate(self, id: int) -> bool:
        rate = self.repository.get_by_id(id)
        if not rate:
            raise NotFoundError(f"Cashback rate with {id} id not found.")
        return self.repository.delete(rate)
