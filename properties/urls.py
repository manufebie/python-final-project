from django.urls import path

from .views import visitor as visitor_views

app_name = 'properties'

urlpatterns = [
    path('houses/', visitor_views.HouseListView.as_view(), name='house_list'),
    path('<slug:slug>/', visitor_views.HouseDetailView.as_view(), name='house_detail'),
]
