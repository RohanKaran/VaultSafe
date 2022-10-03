from datetime import datetime, timezone, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.core import config
from app.core.security import get_password_hash
from app.core.utils import random_hash
from app.crud.base import CRUDBase
from app.models import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, user: UserCreate) -> User:
        new_user = User(
            id=random_hash(),
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
        )
        return self._create_db_object(db=db, db_obj=new_user)

    def get_by_email(self, db: Session, *, email: str):
        return db.query(User).where(User.email == email).first()

    def get_by_username(self, db: Session, *, username: str):
        return db.query(User).where(User.username == username).first()

    def get_session_token(self, db: Session, *, db_obj: User) -> Optional[str]:
        if (
            db_obj.session_token
            and db_obj.session_expiration
            and (
                db_obj.session_expiration
                > datetime.now(db_obj.session_expiration.tzinfo)
            )
        ):
            return db_obj.session_token
        return self.create_session_token(db, db_obj)

    def create_session_token(self, db: Session, db_obj: User) -> Optional[str]:
        db_obj.session_token = random_hash()  # type: ignore
        db_obj.session_expiration = datetime.now(timezone.utc) + timedelta(
            days=config.SESSION_TOKEN_EXPIRE_DAYS
        )

        db_obj = self._create_db_object(db=db, db_obj=db_obj)
        return db_obj.session_token

    def get_by_session_token(
        self, db: Session, *, session_token: str
    ) -> Optional[User]:
        user = db.query(User).filter(User.session_token == session_token).first()  # type: ignore
        if not user or user.session_expiration < datetime.now(
            user.session_expiration.tzinfo
        ):
            return None
        return user


crud_user = CRUDUser(User)
