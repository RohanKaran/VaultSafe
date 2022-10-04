from sqlalchemy.orm import Session

from app.database.init_db import init_db
from app.database.session import SessionLocal


def init() -> None:
    db: Session = SessionLocal()
    init_db(db)


def main() -> None:
    print("Creating initial data")
    init()
    print("Initial data created")


if __name__ == "__main__":
    main()
