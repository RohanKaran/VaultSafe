from sqlalchemy import String, Column, DateTime, func

from app.database.base import Base


class User(Base):
    id = Column(String(64), primary_key=True)
    username = Column(String(64), index=True, unique=True, nullable=False)
    email = Column(String(64), index=True, unique=True, nullable=False)
    password = Column(String(80))
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )
    session_token = Column(String(64))
    session_expiration = Column(DateTime)
