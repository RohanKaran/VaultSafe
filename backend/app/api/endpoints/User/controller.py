from typing import Any

from fastapi import Body, Depends
from fastapi import Path, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.models import User
from app.schemas.generic import Response
from app.schemas.token import Token
from app.schemas.user import UserClient, UserCreateClient
from . import api
from .service import UserService


@api.post("/register/", response_model=Response)
def register(
    request: Request,
    db: Session = Depends(deps.get_db),
    user: UserCreateClient = Body(...),
) -> Any:
    """
    Register new user.
    """
    return Response(
        detail=UserService.register(
            db=db, user=user, server_host=request.headers.get("origin")
        )
    )


@api.post("/create/{token}/", response_model=UserClient, status_code=201)
def create(
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    token: str = Path(...),
) -> Any:
    """
    Create a new user
    """
    return UserService.create(db=db, token=token, password=password)


@api.get("/", response_model=UserClient)
async def get_current_user(
    user: UserClient = Depends(deps.get_current_user),
) -> UserClient:
    """
    Get current user's details
    """
    return user


@api.post("/login/access-token/", response_model=Token)
def get_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    token = UserService.get_access_token(
        db=db, email=form_data.username, password=form_data.password
    )
    return Token(**token)


@api.get("/login/session-token/", response_model=Token)
def get_session_token(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Token:
    """
    Get session token.
    """
    return UserService.get_session_token(db=db, user=current_user)


@api.get("/get-by-user-id/{user_id}/", response_model=UserClient)
def get_by_user_id(db: Session = Depends(deps.get_db), user_id: str = Path(...)) -> Any:
    return UserService.get_by_user_id(db=db, user_id=user_id)


@api.get("/refresh-token/{session_token}/", response_model=Token)
def session_token_login(
    session_token: str = Path(...), db: Session = Depends(deps.get_db)
) -> Any:
    """
    Refresh access token using the session token.
    """
    return Token(**UserService.login_refresh_token(db=db, session_token=session_token))
