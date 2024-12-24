from typing import Optional

from pydantic import ConfigDict, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI app"
    DATABASE_URL: Optional[PostgresDsn] = None

    model_config = ConfigDict(case_sensitive=True)


settings = Settings()
