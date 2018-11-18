'''
This module contains all the views for the agent.
The views allows the agent to do CRUD operations on the aparmentunit object
'''
from .base import *

from ..models import Apartment, ApartmentUnit


class ApartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Apartment
    fields = ['name', 'slug', 'description', 'floors', 'shopping_mall',
        'gym', 'swimming_pool', 'jogging_track', 'laundry', 'security', 'image']
    success_message = 'Apartment %(name)s successfully added'


class MyApartmentUnitListView(LoginRequiredMixin, ListView):
    model = ApartmentUnit
    template_name = 'properties/my_apartment_unit.html'


class ApartmentUnitCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ApartmentUnit
    fields = ['apartment', 'title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'size', 'water_heating', 'available', 
        'floor', 'balcony','image']
    success_message = 'Unit "%(title)s" successfully added'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentUnitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ApartmentUnit
    fields = ['apartment', 'title', 'slug', 'deposit', 'rent_per_month', 'description',
        'furnishing', 'bedrooms', 'bathrooms', 'floors', 'size', 'water_heating', 'available', 
        'floor', 'balcony','image', 'available']
    success_message = '%(title)s successfully updated'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentUnitDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ApartmentUnit
    success_url = reverse_lazy('account:apartmentunit_list')
    success_message = '%(title)s has been deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ApartmentUnitDeleteView, self).delete(request, *args, **kwargs)


    
