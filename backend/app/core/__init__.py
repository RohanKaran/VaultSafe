from functools import lru_cache
from typing import Union

from dotenv import dotenv_values

from .config import DevelopmentConfig, ENV_FILE, ProductionConfig


@lru_cache()
def get_settings() -> Union[DevelopmentConfig, ProductionConfig]:
    env_values = dotenv_values(ENV_FILE)
    env_name = str(env_values.get("ENV", "DEV")).upper()
    parsed_values = {key: value for key, value in env_values.items() if value is not None}
    return (
        DevelopmentConfig(**parsed_values)
        if env_name == "DEV"
        else ProductionConfig(**parsed_values)
    )


config = get_settings()
