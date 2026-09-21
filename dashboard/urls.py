from django.urls import path
from .views import DashboardSummaryView,dashboard_home

urlpatterns = [
    path("summary/",DashboardSummaryView.as_view(),name="dashboard-summary"),
    path("",dashboard_home,name="dashboard-home")
]