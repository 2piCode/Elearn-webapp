from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def relevance(request):
    return render(request, 'main/relevance.html')


def geography(request):
    return render(request, 'main/geography.html')


def skills(request):
    return render(request, 'main/skills.html')


def last_vacancies(request):
    return render(request, 'main/last_vacancies.html')
