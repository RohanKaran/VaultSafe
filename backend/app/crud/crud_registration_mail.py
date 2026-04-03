from sqlalchemy.orm import Session
from sqlalchemy import select

from ..core.utils import random_hash
from ..crud.base import CRUDBase
from ..models.registration_mail import RegistrationMail
from ..schemas.registration_mail import RegistrationMailCreate, RegistrationMailUpdate


class CRUDRegistrationMail(
    CRUDBase[RegistrationMail, RegistrationMailCreate, RegistrationMailUpdate]
):
    def create(self, db: Session, *, obj_in: RegistrationMailCreate) -> RegistrationMail:
        return self._create_db_object(
            db=db, db_obj=RegistrationMail(id=random_hash(), email=obj_in.email)
        )

    def get_by_email(self, db: Session, *, email: str) -> RegistrationMail | None:
        return (
            db.execute(select(RegistrationMail).where(RegistrationMail.email == email))
            .scalars()
            .first()
        )


crud_registration_mail = CRUDRegistrationMail(RegistrationMail)
