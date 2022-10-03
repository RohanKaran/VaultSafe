from functools import lru_cache
from typing import Union

from .config import Config, DevelopmentConfig, ProductionConfig


@lru_cache()
def get_settings() -> Union[DevelopmentConfig, ProductionConfig]:
    return (
        DevelopmentConfig() if Config().dict()["ENV"] == "DEV" else ProductionConfig()
    )


config = get_settings()
