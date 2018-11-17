from django.urls import path

from .views import agent_dashboard, AgentProfileView
from properties.views.agent import HouseCreateView, MyHouseListView

app_name = 'account'

urlpatterns = [
    path('', agent_dashboard, name='dashboard_home'),
    path('my-houses/', MyHouseListView.as_view(), name='house_list'),
    path('add-house/', HouseCreateView.as_view(), name='create_house'),
    path('<slug:slug>/', AgentProfileView.as_view(), name='profile'),
]
