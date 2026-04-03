import re
from pathlib import Path
from typing import Any, ClassVar, Optional, Pattern, Union

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Config(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = False
    SECRET_SALT: str
    ENV: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SESSION_TOKEN_EXPIRE_DAYS: int = 7
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 24

    # Sendgrid Config
    SENDGRID_APIKEY: str = ""
    EMAIL_FROM: str = ""
    EMAIL_BCC: str = ""

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE), env_file_encoding="utf-8", extra="ignore"
    )


class DevelopmentConfig(Config):
    DEBUG: bool = True
    POSTGRES_SERVER: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_URI: str = ""

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: Any) -> str:
        if v:
            return v
        return f"postgresql://{info.data.get('POSTGRES_USER')}:{info.data.get('POSTGRES_PASSWORD')}@{info.data.get('POSTGRES_SERVER')}/{info.data.get('POSTGRES_DB') or ''}"

    FRONTEND_URL: str = "http://localhost:3000"
    FRONTEND_URL_REGEX: ClassVar[Pattern[str]] = re.compile(
        r"^http://(localhost|127\.0\.0\.1):3000$"
    )
    DOCS_URL: Optional[str] = "/docs"


class ProductionConfig(Config):
    POSTGRES_SERVER: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_URI: str = ""

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: Any) -> str:
        if v:
            return v
        return f"postgresql://{info.data.get('POSTGRES_USER')}:{info.data.get('POSTGRES_PASSWORD')}@{info.data.get('POSTGRES_SERVER')}/{info.data.get('POSTGRES_DB') or ''}"

    FRONTEND_URL: str = "https://vaultsafe.netlify.app"
    FRONTEND_URL_REGEX: ClassVar[Pattern[str]] = re.compile(
        "^https://deploy-preview-.*--vaultsafe.netlify.app$"
    )
    DOCS_URL: Optional[str] = None
