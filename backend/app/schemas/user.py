from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreateClient(UserBase):
    password: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserClient(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserClient):
    password: str
