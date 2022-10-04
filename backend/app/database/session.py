from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..core import config

if config.ENV == "DEV":
    engine = create_engine(
        config.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},  # for sqlite
    )
else:
    engine = create_engine(
        config.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
        # connect_args={"check_same_thread": False},  # for sqlite
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
