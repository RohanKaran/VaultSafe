import re
from typing import Any, Dict, Optional, Union

from pydantic import BaseSettings, validator
from pydantic.networks import PostgresDsn


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

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

    FRONTEND_URL = "*"
    FRONTEND_URL_REGEX = re.compile("/*/")


class ProductionConfig(Config):
    # SQLAlchemy config
    POSTGRES_SERVER: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_URI: Union[Optional[PostgresDsn], str]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return v or PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    FRONTEND_URL = "https://vaultsafe.netlify.app"
    FRONTEND_URL_REGEX = re.compile("^https://deploy-preview-.*--vaultsafe.netlify.app")
