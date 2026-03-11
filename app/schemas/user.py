from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class UserDTO(BaseModel):
    id: int | None = Field(None, description="Primary key for the user.")
    username: str = Field(..., description="Full name of the user.")
    created_datetime: datetime | None = Field(
        None, description="Created datetime for the user."
    )
    updated_datetime: datetime | None = Field(
        None, description="Updated datetime for the user."
    )


class UserCreateRequest(BaseModel):
    username: str = Field(..., description="Full name of the user.")

    @field_validator("username", mode="before")
    @classmethod
    def normalize_username(cls, value: str) -> str:
        return value.strip().title()


class UserUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the user.")
    username: str = Field(..., description="Full name of the user.")
