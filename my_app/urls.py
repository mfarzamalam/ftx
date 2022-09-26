from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('about/', about_view, name='about_view'),
    path('services/', services_view, name='services_view'),
    path('accounts/', accounts_view, name='accounts_view'),
    path('contact/', contact_view, name='contact_view'),
]
