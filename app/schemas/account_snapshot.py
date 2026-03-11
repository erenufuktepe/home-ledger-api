from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class AccountSnapshotDTO(BaseModel):
    id: int = Field(..., description="Primary key for the account snapshot.")
    account_id: int = Field(..., description="Related account id.")
    balance: Decimal = Field(
        ..., description="Account balance at snapshot time.", example=2525.4
    )
    snapshot_datetime: datetime = Field(..., description="Datetime of this snapshot.")
    created_datetime: datetime | None = Field(
        None, description="Snapshot row created datetime."
    )
    updated_datetime: datetime | None = Field(
        None, description="Snapshot row updated datetime."
    )


class AccountSnapshotCreateRequest(BaseModel):
    account_id: int = Field(..., description="Related account id.")
    balance: Decimal = Field(
        ..., description="Account balance at snapshot time.", example=2525.4
    )
    snapshot_datetime: datetime = Field(..., description="Datetime of this snapshot.")


class AccountSnapshotUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the account snapshot.")
    account_id: int = Field(..., description="Related account id.")
    balance: Decimal = Field(
        ..., description="Account balance at snapshot time.", example=2525.4
    )
    snapshot_datetime: datetime = Field(..., description="Datetime of this snapshot.")
