from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreateClient(UserBase):
    pass


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserClient(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserInDB(UserClient):
    password: str
