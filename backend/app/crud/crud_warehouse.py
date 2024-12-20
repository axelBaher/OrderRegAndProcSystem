#   region IMPORT
from typing import Type
from sqlalchemy.orm import Session

from backend.app import models as m


#   endregion

#   region READ_WAREHOUSE
def db_get_warehouse_list(db: Session) -> list[Type[m.Warehouse]] | None:
    warehouse_list = db.query(m.Warehouse).filter(m.Warehouse.deleted == 0).all()
    return warehouse_list


def db_get_warehouse(warehouse_id: int, db: Session) -> Type[m.Warehouse] | None:
    warehouse = db.query(m.Warehouse).filter(m.Warehouse.id == warehouse_id, m.Warehouse.deleted == 0).first()
    return warehouse


def db_get_warehouse_item_list(warehouse_id: int, db: Session) -> list[Type[m.WarehouseItem]] | None:
    warehouse_item_list = db.query(m.WarehouseItem).filter(m.WarehouseItem.warehouse_id == warehouse_id,
                                                           m.WarehouseItem.deleted == 0).all()
    return warehouse_item_list

#   endregion

#   region CREATE_WAREHOUSE

#   endregion

#   region UPDATE_WAREHOUSE

#   endregion

#   region DELETE_WAREHOUSE

#   endregion
