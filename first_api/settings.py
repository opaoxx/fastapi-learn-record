from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "First FastAPI API"
    environment: str = "development"
    api_key: str = "dev-secret-key"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FIRST_API_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
