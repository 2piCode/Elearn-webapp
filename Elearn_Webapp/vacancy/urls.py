from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('relevance_load', views.relevance_load, name='relevance_load'),
    path('relevance', views.relevance, name='relevance'),
    path('geography_load', views.geography_load, name='geography_load'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('last_vacancies', views.last_vacancies, name='last')
]
