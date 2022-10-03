from pydantic import BaseModel


class Response(BaseModel):
    detail: str
