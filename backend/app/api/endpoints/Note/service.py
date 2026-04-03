from typing import List

from app import crud
from app.models.note import Note
from app.schemas.generic import Response
from app.schemas.note import NoteCreate, NoteCreateClient, NoteUpdate
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status


class NoteService:
    @staticmethod
    def add_note(db: Session, user_id: str, note: NoteCreateClient) -> Response:
        created_note = crud.crud_note.create(
            db=db,
            obj_in=NoteCreate(content=note.content, user_id=user_id, title=note.title),
        )
        if not created_note:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully created")

    @staticmethod
    def get_note_by_id(db: Session, id: str) -> Note:
        note = crud.crud_note.get(db=db, id=id)
        if not note:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
            )
        return note

    @staticmethod
    def get_all_by_user_id(db: Session, user_id: str) -> List[Note]:
        return crud.crud_note.get_all_by_user_id(db=db, user_id=user_id)

    @staticmethod
    def delete_by_id(db: Session, id: str, user_id: str) -> Response:
        note = crud.crud_note.get(db=db, id=id)
        if (not note) or note.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Request"
            )
        deleted_note = crud.crud_note.remove(db=db, id=id)
        if not deleted_note:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully deleted")

    @staticmethod
    def update_by_id(
        db: Session, id: str, user_id: str, note_update: NoteUpdate
    ) -> Response:
        note = crud.crud_note.get(db=db, id=id)
        if (not note) or note.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Request"
            )
        updated_note = crud.crud_note.update(
            db=db,
            db_obj=note,
            obj_in=NoteUpdate(title=note_update.title, content=note_update.content),
        )
        if not updated_note:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully updated")
