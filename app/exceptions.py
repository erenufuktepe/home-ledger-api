from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional


@dataclass
class AppError(Exception):
    message: str
    code: str = "app_error"
    status_code: int = 400
    details: Optional[Mapping[str, Any]] = None

    def __str__(self) -> str:
        return self.message


class UserNotFoundError(AppError):
    def __init__(self, id: int, *, details=None):
        super().__init__(
            message=f"User with {id} id not found.",
            code="not_found",
            status_code=404,
            details=details,
        )


class UserExistsError(AppError):
    def __init__(self, username: str, *, details=None):
        super().__init__(
            message=f"User {username} already exists.",
            code="not_found",
            status_code=409,
            details=details,
        )


class NotFoundError(AppError):
    def __init__(self, message: str = "Resource not found", *, details=None):
        super().__init__(
            message=message, code="not_found", status_code=404, details=details
        )


class ConflictError(AppError):
    def __init__(self, message: str = "Conflict", *, details=None):
        super().__init__(
            message=message, code="conflict", status_code=409, details=details
        )


class ValidationError(AppError):
    def __init__(self, message: str = "Validation failed", *, details=None):
        super().__init__(
            message=message, code="validation_error", status_code=422, details=details
        )
