from django.urls import path
from .views import landing_index

# Adds site header, site title, index title to the admin side.

urlpatterns = [
    path('', landing_index, name='landing-webfilter'),
]

