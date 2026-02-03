from datetime import datetime

from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    id: int | None = Field(None, description="Primary key for the user.")
    username: str = Field(..., description="Full name of the user.")
    created_at: datetime | None = Field(
        datetime.now(), description="Created datetime for the user."
    )


class UserCreateRequest(BaseModel):
    username: str = Field(..., description="Full name of the user.")


class UserUpdateRequest(BaseModel):
    id: int = Field(..., description="Primary key for the user.")
    username: str = Field(..., description="Full name of the user.")
