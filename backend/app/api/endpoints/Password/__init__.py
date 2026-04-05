from fastapi import APIRouter  # pyright: reportUnusedImport=false

api = APIRouter()

from . import controller as controller  # noqa: E402
