from fastapi import APIRouter

from .endpoints.Note import api as note_api
from .endpoints.Password import api as password_api
from .endpoints.User import api as user_api

api: APIRouter = APIRouter()

api.include_router(user_api, tags=["User"], prefix="/user")
api.include_router(password_api, tags=["Password"], prefix="/password")
api.include_router(note_api, tags=["Note"], prefix="/note")
