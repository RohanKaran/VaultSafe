from datetime import datetime

from pydantic import BaseModel, EmailStr


class RegistrationMailBase(BaseModel):
    email: EmailStr


class RegistrationMailCreate(RegistrationMailBase):
    pass


class RegistrationMailUpdate(RegistrationMailBase):
    pass


class RegistrationMailClient(RegistrationMailBase):
    id: str
    datetime: datetime
    email: EmailStr

    class Config:
        orm_mode = True
