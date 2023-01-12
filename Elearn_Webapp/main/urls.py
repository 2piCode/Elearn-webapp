from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('relevance', views.relevance),
    path('geography', views.geography),
    path('skills', views.skills),
    path('last', views.last_vacancies)
]
