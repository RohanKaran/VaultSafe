from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .api import api
from .core import config
from .schemas.generic import Response


def create_app():
    app = FastAPI(
        title="VaultSafe",
        version="0.2.0",
        description="VaultSafe Backend APIs",
        debug=True,
        docs_url=config.DOCS_URL,
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
        allow_origin_regex=config.FRONTEND_URL_REGEX,
    )


def health_checkup(app: FastAPI):
    @app.get("/health")
    def health_check():
        return Response(detail="Hey there!")
