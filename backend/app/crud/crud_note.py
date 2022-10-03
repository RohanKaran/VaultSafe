from typing import List

from sqlalchemy.orm import Session

from ..core.utils import random_hash
from ..crud.base import CRUDBase
from ..models import Note
from ..schemas.note import NoteCreate, NoteUpdate


class CRUDNote(CRUDBase[Note, NoteCreate, NoteUpdate]):
    def create(self, db: Session, *, obj_in: NoteCreate) -> Note:
        note = Note(
            id=random_hash(),
            user_id=obj_in.user_id,
            title=obj_in.title,
            content=obj_in.content,
        )
        return self._create_db_object(db=db, db_obj=note)

    def get_all_by_user_id(self, db: Session, *, user_id: str) -> List[Note]:
        return db.query(Note).where(Note.user_id == user_id).all()


crud_note = CRUDNote(Note)
