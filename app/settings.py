from pathlib import Path
from zoneinfo import ZoneInfo

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    TZ: str = "America/Chicago"
    DATABASE_URL: str
    DEBUG: bool = False
    CORS_ALLOW_ORIGINS: str

    @property
    def tzinfo(self):
        return ZoneInfo(self.TZ)

    @property
    def cors_allow_origins(self) -> list[str]:
        if not self.CORS_ALLOW_ORIGINS:
            return []
        return [
            origin.strip()
            for origin in self.CORS_ALLOW_ORIGINS.split(",")
            if origin.strip()
        ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = ","


settings = Settings()
