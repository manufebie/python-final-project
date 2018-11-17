
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

from accounts.views import AgentRegistrationView, AgentProfileCreateView
from pages.views import about_page, home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about_page, name='about'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', AgentRegistrationView.as_view(), name='register'),
    path('register/success/', AgentProfileCreateView.as_view(), name='registration_success'),

    path('account/', include('accounts.urls')),
]
