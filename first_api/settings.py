from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "First FastAPI API"
    environment: str = "development"
    api_key: str = "dev-secret-key"
    ai_provider: Literal["demo"] = "demo"
    ai_provider_health_url: str = "https://example.com"
    ai_timeout_seconds: float = Field(default=10.0, gt=0)
    ai_max_attempts: int = Field(default=1, ge=1, le=5)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FIRST_API_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
