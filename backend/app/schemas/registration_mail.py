from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class RegistrationMailBase(BaseModel):
    email: EmailStr


class RegistrationMailCreate(RegistrationMailBase):
    pass


class RegistrationMailUpdate(RegistrationMailBase):
    pass


class RegistrationMailClient(RegistrationMailBase):
    id: str
    sent_at: datetime
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
