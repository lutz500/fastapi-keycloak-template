from typing import Optional

from pydantic import ConfigDict, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI app"

    # Database settings
    DATABASE_URL: Optional[PostgresDsn] = None

    # Keycloak settings
    KEYCLOAK_SERVER_URL: str = "http://localhost:8080"
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_CLIENT_SECRET: str
    ALGORITHM: str
    MODE: str = "DEV"

    model_config = ConfigDict(case_sensitive=True)


settings = Settings()
