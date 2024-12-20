#   region IMPORT
from fastapi import APIRouter, Depends

from backend.app.crud.crud_debug import *
from backend.app.dependencies import get_db

#   endregion
DebugRouter = APIRouter()


@DebugRouter.get(
    path="/fill"
)
def fill_database(db: Session = Depends(get_db)):
    db_fill_database(db=db)


@DebugRouter.post(
    path="/clear"
)
def clear_database(db: Session = Depends(get_db)):
    db_clear_database(db=db)
