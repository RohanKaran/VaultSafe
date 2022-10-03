from typing import Any, List

from fastapi import Body, Depends, Path
from sqlalchemy.orm import Session

from app.schemas.generic import Response
from app.schemas.password import PasswordClient, PasswordCreateClient, PasswordUpdate
from app.schemas.user import UserClient
from . import api
from .service import PasswordService
from ... import deps


@api.post("/add-password/", response_model=Response, status_code=201)
def create_password(
    db: Session = Depends(deps.get_db),
    password: PasswordCreateClient = Body(...),
    user: UserClient = Depends(deps.get_current_user),
) -> Any:
    return PasswordService.add_password(db=db, password=password, user_id=user.id)


@api.get("/get-password-by-id/{password_id}/", response_model=PasswordClient)
def get_by_id(db: Session = Depends(deps.get_db), password_id: str = Path(...)) -> Any:
    return PasswordService.get_password_by_id(db=db, id=password_id)


@api.get("/", response_model=List[PasswordClient])
def get_all(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
) -> Any:
    return PasswordService.get_all_by_user_id(db=db, user_id=user.id)


@api.delete("/delete/{password_id}/", response_model=Response)
def delete_password_by_id(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
    password_id: str = Path(...),
) -> Any:
    return PasswordService.delete_by_id(db=db, id=password_id, user_id=user.id)


@api.put("/update/{password_id}/")
def update_password_by_id(
    db: Session = Depends(deps.get_db),
    user: UserClient = Depends(deps.get_current_user),
    password_id: str = Path(...),
    password_update: PasswordUpdate = Body(...),
) -> Any:
    return PasswordService.update_by_id(
        db=db, id=password_id, user_id=user.id, password_update=password_update
    )
