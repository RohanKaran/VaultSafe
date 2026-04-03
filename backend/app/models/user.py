from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(64), index=True, unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(64), index=True, unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(80))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.current_timestamp()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )
    session_token: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    session_expiration: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
