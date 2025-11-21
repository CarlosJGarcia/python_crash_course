""" Defines URL patterns for meal_plans."""

from . import views
from django.urls import path

app_name = 'meal_plans'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
