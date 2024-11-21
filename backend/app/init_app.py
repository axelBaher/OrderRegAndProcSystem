from fastapi import FastAPI

from backend.app.api.router import MainRouter
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    application = FastAPI()
    return application


def init_routers(app_: FastAPI) -> None:
    app_.include_router(MainRouter)


def init_cors(app_: FastAPI) -> None:
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
