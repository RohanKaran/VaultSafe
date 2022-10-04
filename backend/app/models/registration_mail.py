from datetime import datetime

from sqlalchemy import Column, DateTime, String

from app.database import Base


class RegistrationMail(Base):
    id = Column(String(64), primary_key=True)
    email = Column(String(64), nullable=False, index=True, unique=True)
    datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)