from typing import Dict

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.core import security, utils
from app.core.security import verify_password
from app.models.user import User
from app.schemas.token import Token, TokenPayload
from app.schemas.user import UserCreate, UserCreateClient


class UserService:
    @staticmethod
    def register(db: Session, user: UserCreateClient, server_host: str) -> str:
        if crud.crud_user.get_by_email(db=db, email=user.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )
        token = utils.generate_new_account_token(
            email=user.email,
            username=user.username,
        )

        verification_mail = utils.send_new_account_email(
            email_to=user.email,
            token=token,
            username=user.username,
            server_host=server_host,
        )

        if not verification_mail:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Could not send email."
            )

        return "Email Sent"

    @staticmethod
    def create(db: Session, token: str, password: str) -> User:
        token_payload = utils.verify_new_account_token(token)
        if not token_payload:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The token is invalid or expired.",
            )

        _token_payload = TokenPayload(**token_payload)
        if crud.crud_user.get_by_email(db=db, email=_token_payload.user_email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email is already registered. If it's your email, please sign in.",
            )
        if crud.crud_user.get_by_username(db=db, username=_token_payload.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username not available."
            )
        user = crud.crud_user.create(
            db=db,
            user=UserCreate(
                username=_token_payload.username,
                email=_token_payload.user_email,
                password=password,
            ),
        )
        return user

    @staticmethod
    def get_access_token(db: Session, email: str, password: str) -> Dict[str, str]:
        user = crud.crud_user.get_by_email(db=db, email=email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )
        elif not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Password!"
            )
        return {
            "access_token": security.create_access_token({"user_email": user.email}),
            "token_type": "bearer",
        }

    @staticmethod
    def login_refresh_token(db: Session, session_token: str) -> Dict[str, str]:
        """
        Log in with session token.
        """
        user = crud.crud_user.get_by_session_token(db, session_token=session_token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect session token",
            )

        return {
            "access_token": security.create_access_token({"user_email": user.email}),
            "token_type": "bearer",
        }

    @staticmethod
    def get_session_token(db: Session, user: User) -> Token:

        token = crud.crud_user.get_session_token(db, db_obj=user)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The token couldn't be created.",
            )
        return Token(access_token=token, token_type="session")

    @staticmethod
    def get_by_user_id(db: Session, user_id: str) -> User:
        user = crud.crud_user.get(id=user_id, db=db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )
        return user
