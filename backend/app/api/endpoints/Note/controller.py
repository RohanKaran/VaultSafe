from typing import Any, List

from fastapi import Body, Depends, Path
from sqlalchemy.orm import Session

from app.schemas.generic import Response
from app.schemas.note import NoteClient, NoteCreateClient, NoteUpdate
from app.schemas.user import UserClient

from ... import deps
from . import api
from .service import NoteService


@api.post("/add-note/", response_model=Response, status_code=201)
def create_note(
    db: Session = Depends(deps.get_db),
    note: NoteCreateClient = Body(...),
    user: UserClient = Depends(deps.get_current_user),
) -> Any:
    return NoteService.add_note(db=db, note=note, user_id=user.id)


@api.get("/get-note-by-id/{note_id}/", response_model=NoteClient)
def get_by_id(db: Session = Depends(deps.get_db), note_id: str = Path(...)) -> Any:
    return NoteService.get_note_by_id(db=db, id=note_id)


@api.get("/", response_model=List[NoteClient])
def get_all(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
) -> Any:
    return NoteService.get_all_by_user_id(db=db, user_id=user.id)


@api.delete("/delete/{note_id}/", response_model=Response)
def delete_note_by_id(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
    note_id: str = Path(...),
) -> Any:
    return NoteService.delete_by_id(db=db, id=note_id, user_id=user.id)


@api.put("/update/{note_id}/")
def update_note_by_id(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
    note_id: str = Path(...),
    note_update: NoteUpdate = Body(...),
) -> Any:
    return NoteService.update_by_id(
        db=db, id=note_id, user_id=user.id, note_update=note_update
    )
