from django.urls import path

from .views import agent_dashboard, AgentProfileView, AgentSubmitDocumentView
from properties.views.agent import (HouseCreateView, MyHouseListView, HouseUpdateView,
                                    HouseDeleteView)

app_name = 'account'

urlpatterns = [
    path('', agent_dashboard, name='dashboard_home'),
    path('my-houses/', MyHouseListView.as_view(), name='house_list'),
    path('<slug:slug>/update/', HouseUpdateView.as_view(), name='update_house'),
    path('<slug:slug>/delete/', HouseDeleteView.as_view(), name='delete_house'),
    path('add-house/', HouseCreateView.as_view(), name='create_house'),
    path('submit-document/', AgentSubmitDocumentView.as_view(), name='submit_document'),
   
    path('<slug:slug>/', AgentProfileView.as_view(), name='profile'),
]
