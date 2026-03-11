import enum

from fastapi import APIRouter

from app.enums import AccountType, Frequency, IncomeType, PaymentPurpose, SpendingCategory
from app.schemas import EnumOptionDTO, MetadataDTO

router = APIRouter(tags=["Metadata"])


def _to_options(enum_type: type[enum.Enum]) -> list[EnumOptionDTO]:
    return [EnumOptionDTO(key=item.name, value=item.value) for item in enum_type]


@router.get("/metadata", status_code=200)
async def get_metadata() -> MetadataDTO:
    return MetadataDTO(
        account_types=_to_options(AccountType),
        frequencies=_to_options(Frequency),
        income_types=_to_options(IncomeType),
        payment_purposes=_to_options(PaymentPurpose),
        spending_categories=_to_options(SpendingCategory),
    )
