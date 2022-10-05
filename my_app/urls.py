from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .forms import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('accounts/', accounts_view, name='accounts'),
    path('contact/', contact_view, name='contact'),
    path(
        "login/",
        LoginView.as_view(
            template_name="login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
