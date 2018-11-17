from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from core_app.models import CustomUser
from .forms import AgentRegistrationForm, AgentProfileForm
from .models import Agent


class AgentRegistrationView(CreateView):
    model = CustomUser
    form_class = AgentRegistrationForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        '''Authenticate the user after registering and redirect them
        to AgentProfileCreate'''
        user = form.save()
        login(self.request, user)
        return redirect('registration_success')


class AgentProfileCreateView(LoginRequiredMixin, CreateView):
    model = Agent
    form_class = AgentProfileForm
    template_name = 'registration/registration_success.html'
    success_url = reverse_lazy('account:dashboard_home')

    def form_valid(self, form):
        # assign user to requested user
        form.instance.user = self.request.user
        return super().form_valid(form)


class AgentProfileView(LoginRequiredMixin, DetailView):
    model = Agent
    template_name = 'accounts/agent_profile.html'


def agent_dashboard(request):
    return render(request, 'accounts/dashboard_home.html', {})    