from django.shortcuts import render
from .models import Vacancy

def vacancy_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy_home.html', {'vacancies': vacancies})
