from sqlalchemy.orm import Session
from .. import crud

from .session import engine
from ..core.security import get_password_hash
from ..core.utils import random_hash
from ..database import Base
from ..models import User


def init_db(db: Session) -> None:

    Base.metadata.create_all(bind=engine)

    crud.crud_user.create(
        db=db,
        user=User(
            id=random_hash(),
            username="localuser",
            email="user@example.com",
            password=get_password_hash("localpassword"),
        ),
    )
