from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PasswordBase(BaseModel):
    title: str
    password: str
    iv: str
    username: str


class PasswordCreateClient(PasswordBase):
    website: Optional[str] = None


class PasswordUpdate(PasswordCreateClient):
    pass


class PasswordCreate(PasswordCreateClient):
    user_id: str


class PasswordClient(PasswordBase):
    id: str
    user_id: str
    website: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
