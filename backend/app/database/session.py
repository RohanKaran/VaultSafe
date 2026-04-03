from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..core import config

database_uri = str(config.SQLALCHEMY_DATABASE_URI)

if database_uri.startswith("sqlite"):
    engine = create_engine(
        database_uri,
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},  # for sqlite
    )
else:
    engine = create_engine(
        database_uri,
        pool_pre_ping=True,
        # connect_args={"check_same_thread": False},  # for sqlite
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
