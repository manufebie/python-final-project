from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from core_app.models import CustomUser
from .models import Agent, ContentManager

class AgentRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_agent = True
        user.save()
        return user


class AgentProfileForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['name', 'slug', 'is_company', 'is_independent',
            'about', 'phonenumber', 'line_id']


