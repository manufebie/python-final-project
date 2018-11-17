from django.urls import path

from .views import agent_dashboard, AgentProfileView

app_name = 'account'

urlpatterns = [
    path('', agent_dashboard, name='dashboard_home'),
    path('<slug:slug>/', AgentProfileView.as_view(), name='profile'),
]
