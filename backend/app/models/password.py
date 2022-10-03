from sqlalchemy import Column, DateTime, ForeignKey, String, func

from ..database.base import Base


class Password(Base):
    id = Column(String(64), primary_key=True)
    user_id = Column(String(64), ForeignKey("user.id", ondelete="CASCADE"))
    title = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    website = Column(String(64))
    password = Column(String(255), nullable=False)
    iv = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )
