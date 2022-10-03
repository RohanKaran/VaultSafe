from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .api import api
from .core import config
from .schemas.generic import Response


def create_app():

    app = FastAPI(
        title="Password Manager",
        version="0.1.0",
        description="Password Manager Backend APIs",
        debug=True,
    )

    register_extensions(app)
    health_checkup(app)

    app.include_router(api, prefix="/api/v1")  # pyright: reportGeneralTypeIssues=false

    return app


def register_extensions(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[config.FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def health_checkup(app: FastAPI):
    @app.get("/health")
    def health_check():
        return Response(detail="Hey there!")
