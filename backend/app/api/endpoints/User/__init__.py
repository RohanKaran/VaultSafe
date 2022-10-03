from fastapi import APIRouter  # pyright: reportUnusedImport=false

api = APIRouter()

from . import controller  # noqa: F401,E402
