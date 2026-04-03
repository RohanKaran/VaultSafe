from datetime import datetime, timedelta, timezone
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..core import config
from ..core.security import get_password_hash
from ..core.utils import random_hash
from ..crud.base import CRUDBase
from ..models import User
from ..schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        new_user = User(
            id=random_hash(),
            username=obj_in.username,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
        )
        return self._create_db_object(db=db, db_obj=new_user)

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.execute(select(User).where(User.email == email)).scalars().first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return (
            db.execute(select(User).where(User.username == username)).scalars().first()
        )

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
        db_obj.session_token = random_hash()
        db_obj.session_expiration = datetime.now(timezone.utc) + timedelta(
            days=config.SESSION_TOKEN_EXPIRE_DAYS
        )

        db_obj = self._create_db_object(db=db, db_obj=db_obj)
        return db_obj.session_token

    def get_by_session_token(
        self, db: Session, *, session_token: str
    ) -> Optional[User]:
        user = (
            db.execute(select(User).filter(User.session_token == session_token))
            .scalars()
            .first()
        )
        if not user or not user.session_expiration:
            return None
        if user.session_expiration < datetime.now(user.session_expiration.tzinfo):
            return None
        return user


crud_user = CRUDUser(User)
