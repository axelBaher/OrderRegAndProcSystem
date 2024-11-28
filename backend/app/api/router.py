from fastapi import APIRouter

from backend.app.api.endpoints.ep_customer import CustomerRouter
from backend.app.api.endpoints.ep_warehouse import WarehouseRouter
from backend.app.api.endpoints.ep_assemblyPoint import AssemblyPointRouter
from backend.app.api.endpoints.ep_debug import DebugRouter
from backend.app.api.endpoints.ep_security import SecurityRouter

__all__ = ["MainRouter"]

MainRouter = APIRouter()

MainRouter.include_router(CustomerRouter, prefix="/customers", tags=["Customer"])
MainRouter.include_router(WarehouseRouter, prefix="/warehouses", tags=["Warehouse"])
MainRouter.include_router(AssemblyPointRouter, prefix="/assembly_points", tags=["Assembly point"])
MainRouter.include_router(DebugRouter, prefix="/debug", tags=["Debug"])
MainRouter.include_router(SecurityRouter, prefix="", tags=["Security"])
