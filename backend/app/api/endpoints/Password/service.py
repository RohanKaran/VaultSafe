from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app import crud
from app.schemas.generic import Response
from app.schemas.password import (PasswordClient, PasswordCreate,
                                  PasswordCreateClient, PasswordUpdate)


class PasswordService:
    @staticmethod
    def add_password(
        db: Session, user_id: str, password: PasswordCreateClient
    ) -> Response:
        password = crud.crud_password.create(
            db=db,
            obj_in=PasswordCreate(
                password=password.password,
                user_id=user_id,
                iv=password.iv,
                title=password.title,
                website=password.website if password.website else None,
                username=password.username,
            ),
        )
        if not password:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully created")

    @staticmethod
    def get_password_by_id(db: Session, id: str) -> PasswordClient:
        return crud.crud_password.get(db=db, id=id)

    @staticmethod
    def get_all_by_user_id(db: Session, user_id: str) -> List[PasswordClient]:
        return crud.crud_password.get_all_by_user_id(db=db, user_id=user_id)

    @staticmethod
    def delete_by_id(db: Session, id: str, user_id: str) -> Response:
        password = crud.crud_password.get(db=db, id=id)
        if (not password) or password.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Request"
            )
        deleted_password = crud.crud_password.remove(db=db, id=id)
        if not deleted_password:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully deleted")

    @staticmethod
    def update_by_id(
        db: Session, id: str, user_id: str, password_update: PasswordUpdate
    ) -> Response:
        password = crud.crud_password.get(db=db, id=id)
        if (not password) or password.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Request"
            )
        updated_password = crud.crud_password.update(
            db=db,
            db_obj=password,
            obj_in=PasswordUpdate(
                password=password_update.password,
                iv=password_update.iv,
                title=password_update.title,
                website=password_update.website if password_update.website else None,
                username=password_update.username,
            ),
        )
        if not updated_password:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="Something went wrong",
            )
        return Response(detail="Successfully updated")
