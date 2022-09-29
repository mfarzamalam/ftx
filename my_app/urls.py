from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('accounts/', accounts_view, name='accounts'),
    path('contact/', contact_view, name='contact'),
]
