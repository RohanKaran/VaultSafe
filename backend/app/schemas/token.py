from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    token: str
    token_type: str


class TokenPayload(BaseModel):
    user_email: EmailStr
    username: str = None
