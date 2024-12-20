#   region IMPORT
from fastapi import APIRouter, Depends, status

from backend.app.crud.crud_assembly_point import *
from backend.app.dependencies import get_db
from backend.app.expection_handler import handle_exceptions

#   endregion

AssemblyPointRouter = APIRouter()


#   region READ_ASSEMBLY_POINT
@AssemblyPointRouter.get(
    path="",
    status_code=status.HTTP_200_OK
)
def get_assembly_point_list(db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_assembly_point_list, query_args={})


@AssemblyPointRouter.get(
    path="/{assembly_point_id}",
    status_code=status.HTTP_200_OK
)
def get_assembly_point(assembly_point_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_assembly_point, query_args={"assembly_point_id": assembly_point_id})

#   endregion

#   region CREATE_ASSEMBLY_POINT

#   endregion

#   region UPDATE_ASSEMBLY_POINT

#   endregion

#   region DELETE_ASSEMBLY_POINT

#   endregion
