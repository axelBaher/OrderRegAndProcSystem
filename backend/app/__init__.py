from fastapi import FastAPI
from backend.app.api import APIRouter


def create_app() -> FastAPI:
    application = FastAPI()
    return application


app = create_app()
# app.include_router(APIRouter())
