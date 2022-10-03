from datetime import datetime

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreateClient(NoteBase):
    pass


class NoteCreate(NoteCreateClient):
    user_id: str
    pass


class NoteUpdate(NoteBase):
    pass


class NoteClient(NoteBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
