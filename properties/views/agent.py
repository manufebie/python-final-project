from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from ..models import House


class MyHouseListView(LoginRequiredMixin, ListView):
    model = House
    template_name = 'properties/agent_house_list.html'

    # only show agent owned property


# view should only be accessable for property agents
class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    fields = ['title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'bathrooms', 'floors', 'size', 'water_heating', 'image']
    template_name = 'properties/house_create_form.html'

    def form_valid(self, form):
        # assign owner field to logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)