from typing import Annotated

from fastapi import APIRouter, Depends

from app.routes.dependencies import get_dashboard_service
from app.schemas import Dashboard
from app.services import DashboardService

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard", status_code=200)
async def get_dashboard(
    service: Annotated[DashboardService, Depends(get_dashboard_service)],
) -> Dashboard:
    return service.get_dashboard()
