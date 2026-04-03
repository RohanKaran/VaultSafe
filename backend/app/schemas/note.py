from datetime import datetime

from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)
