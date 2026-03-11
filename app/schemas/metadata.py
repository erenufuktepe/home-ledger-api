from pydantic import BaseModel, Field


class EnumOptionDTO(BaseModel):
    key: str = Field(..., description="Enum key.")
    value: str = Field(..., description="Enum value.")


class MetadataDTO(BaseModel):
    account_types: list[EnumOptionDTO] = Field(
        ..., description="Supported account types."
    )
    frequencies: list[EnumOptionDTO] = Field(
        ..., description="Supported recurring frequencies."
    )
    income_types: list[EnumOptionDTO] = Field(..., description="Supported income types.")
    payment_purposes: list[EnumOptionDTO] = Field(
        ..., description="Supported payment purposes."
    )
    spending_categories: list[EnumOptionDTO] = Field(
        ..., description="Supported spending categories."
    )
