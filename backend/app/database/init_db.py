from sqlalchemy.orm import Session

from .. import crud
from ..database import Base
from ..schemas.user import UserCreate
from .session import engine


def init_db(db: Session) -> None:

    Base.metadata.create_all(bind=engine)

    crud.crud_user.create(
        db=db,
        user=UserCreate(
            username="localuser",
            email="user@example.com",
            password="localpassword",
        ),
    )
