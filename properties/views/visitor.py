from django.views.generic import ListView, DetailView

from ..models import House


class HouseListView(ListView):
    # List view for houses that are available
    queryset = House.objects.filter(available=True)


class HouseDetailView(DetailView):
    model = House
