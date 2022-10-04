from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud
from app.database.session import SessionLocal
from app.models import User
from app.schemas.token import TokenPayload

from ..core import config, security

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login/access-token/")


def get_db() -> Generator[Session, None, None]:
    """
    Get a database connection
    """
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        ) from e
    user = crud.crud_user.get_by_email(db=db, email=token_data.user_email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
