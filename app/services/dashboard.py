from app.repositories import DashboardRepository
from app.schemas import Dashboard


class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repository = repository

    def get_dashboard(self) -> Dashboard:
        return Dashboard(
            users=self.repository.get_user_summary(),
            payments=self.repository.get_monthly_obligations(),
        )
