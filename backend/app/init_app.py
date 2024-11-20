from fastapi import FastAPI
from backend.app.api.router import MainRouter


def create_app() -> FastAPI:
    application = FastAPI()
    return application


def init_routers(app_: FastAPI) -> None:
    app_.include_router(MainRouter)

