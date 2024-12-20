#   region IMPORT
from typing import Type
from sqlalchemy.orm import Session

from backend.app import models as m


#   endregion

#   region READ_ASSEMBLY_POINT
def db_get_assembly_point_list(db: Session) -> list[Type[m.AssemblyPoint]] | None:
    assembly_point_list = db.query(m.AssemblyPoint).all()
    return assembly_point_list


def db_get_assembly_point(assembly_point_id: int, db: Session) -> Type[m.AssemblyPoint] | None:
    assembly_point = db.query(m.AssemblyPoint).filter(m.AssemblyPoint.id == assembly_point_id,
                                                      m.AssemblyPoint.deleted == 0).first()
    return assembly_point

#   endregion

#   region CREATE_ASSEMBLY_POINT

#   endregion

#   region UPDATE_ASSEMBLY_POINT

#   endregion

#   region DELETE_ASSEMBLY_POINT

#   endregion
