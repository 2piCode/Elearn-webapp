from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_home, name='vacancy_home'),
]
