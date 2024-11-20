#   region IMPORT
from fastapi import APIRouter, Depends, status

from backend.app.crud.crud_warehouse import *
from backend.app.dependencies import get_db
from backend.app.expection_handler import handle_exceptions

#   endregion

WarehouseRouter = APIRouter()


#   region READ_WAREHOUSE
@WarehouseRouter.get(
    path="",
    status_code=status.HTTP_200_OK
)
def get_warehouse_list(db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_warehouse_list, query_args={})


@WarehouseRouter.get(
    path="/{warehouse_id}",
    status_code=status.HTTP_200_OK
)
def get_warehouse(warehouse_id: str, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_warehouse, query_args={"warehouse_id": warehouse_id})


@WarehouseRouter.get(
    path="/{warehouse_id}/warehouse_items",
    status_code=status.HTTP_200_OK
)
def get_warehouse_items(warehouse_id: str, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_warehouse_item_list, query_args={"warehouse_id": warehouse_id})

#   endregion

#   region CREATE_WAREHOUSE

#   endregion

#   region UPDATE_WAREHOUSE

#   endregion

#   region DELETE_WAREHOUSE

#   endregion
