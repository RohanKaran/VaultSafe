from typing import List

from sqlalchemy.orm import Session

from app.core.utils import random_hash
from app.crud.base import CRUDBase
from app.models import Password
from app.schemas.password import PasswordCreate, PasswordUpdate


class CRUDPassword(CRUDBase[Password, PasswordCreate, PasswordUpdate]):
    def create(self, db: Session, *, obj_in: PasswordCreate) -> Password:
        password = Password(
            id=random_hash(),
            user_id=obj_in.user_id,
            password=obj_in.password,
            iv=obj_in.iv,
            title=obj_in.title,
            website=obj_in.website,
            username=obj_in.username,
        )
        return self._create_db_object(db=db, db_obj=password)

    def get_all_by_user_id(self, db: Session, *, user_id: str) -> List[Password]:
        return db.query(Password).where(Password.user_id == user_id).all()


crud_password = CRUDPassword(Password)
