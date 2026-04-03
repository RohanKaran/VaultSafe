from functools import lru_cache
from typing import Union

from pydantic_settings import BaseSettings

from .config import Config, DevelopmentConfig, ProductionConfig


class _SettingsSelector(BaseSettings):
    ENV: str = "DEV"

    model_config = Config.model_config


@lru_cache()
def get_settings() -> Union[DevelopmentConfig, ProductionConfig]:
    env_name = _SettingsSelector().ENV.upper()
    return DevelopmentConfig() if env_name == "DEV" else ProductionConfig()


config = get_settings()
