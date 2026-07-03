from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "First FastAPI API"
    environment: str = "development"
    api_key: str = "dev-secret-key"
    ai_provider: Literal["demo"] = "demo"
    ai_prediction_backend: Literal["demo", "provider"] = "demo"
    ai_provider_health_url: str = "https://example.com"
    ai_provider_prediction_url: str = "https://example.com/predict"
    ai_timeout_seconds: float = Field(default=10.0, gt=0)
    ai_max_attempts: int = Field(default=1, ge=1, le=5)
    ai_retry_base_delay_seconds: float = Field(default=0.1, ge=0)
    ai_retry_max_delay_seconds: float = Field(default=2.0, ge=0)
    ai_retry_jitter_seconds: float = Field(default=0.0, ge=0)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FIRST_API_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
