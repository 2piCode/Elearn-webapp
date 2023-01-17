from django.shortcuts import render
from django.db.models import Q, Count, Avg
from .models import Vacancy

def vacancy_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy_home.html', {'vacancies': vacancies})


def index(request):
    return render(request, 'vacancy/index.html')


def relevance_load(request):
    profession_name = "c++ разработчик"
    name_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='c++')
    header_year = ["Год", "Средняя зарплата", f"Средняя зарплата - {profession_name}", "Количество вакансий",
                   f"Количество вакансий - {profession_name}"]
    count_by_profession_name = Count('id', filter=name_filter)
    salary_by_profession_name = Avg('salary', filter=name_filter)
    statistics_by_years = list(Vacancy.objects
                               .values('published_at')
                               .annotate(total_count=Count('id'), avg_salary=Avg('salary'),
                                         count_by_profession_name=count_by_profession_name,
                                         salary_by_profession_name=salary_by_profession_name)
                               .values('published_at', 'total_count', 'avg_salary',
                                       'count_by_profession_name', 'salary_by_profession_name')
                               .order_by())
    data = {
        'header_year': header_year,
        'profession_name': f"{profession_name}",
        'statistics_by_years': statistics_by_years
    }

    return render(request, 'vacancy/relevance_load.html', data)

def relevance(request):
    return render(request, 'vacancy/relevance.html')


def geography(request):
    return render(request, 'vacancy/geography.html')


def skills(request):
    return render(request, 'vacancy/skills.html')


def last_vacancies(request):
    return render(request, 'vacancy/last_vacancies.html')
