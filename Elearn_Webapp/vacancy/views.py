from django.shortcuts import render
from django.db.models import Q, Count, Avg
from .forms import HHForm
from .models import Vacancy
from collections import Counter
from .HHFinder import HHFinder


def vacancy_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy_home.html', {'vacancies': vacancies})


def index(request):
    return render(request, 'vacancy/index.html')


def relevance_load(request):
    profession_name = "С++ разработчик"
    name_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='c++')
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
        'statistics_by_years': statistics_by_years
    }

    return render(request, 'vacancy/relevance_load.html', data)


def relevance(request):
    return render(request, 'vacancy/relevance.html')


def geography_load(request):
    profession_name = "C++ разработчик"
    name_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='с++')
    count_by_profession_name = Count('id', filter=name_filter)
    statistics_by_cities = list(Vacancy.objects
                                .values('area_name')
                                .annotate(total_count=Count('id'),
                                            avg_salary=Avg('salary'),
                                            count_by_profession_name=count_by_profession_name)
                                .values('area_name', 'total_count', 'avg_salary', 'count_by_profession_name')
                                .order_by('-count_by_profession_name'))
    data = {
        "statistics_by_cities": statistics_by_cities
    }
    return render(request, 'vacancy/geography.html', data)


def geography(request):
    return render(request, 'vacancy/geography.html')


def skills(request):
    return render(request, 'vacancy/skills.html')


def skills_load(request):
    profession_name = "C++ разработчик"
    name_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='с++')
    vancanies_by_profession = Vacancy.objects.filter(name_filter)

    all_skills = vancanies_by_profession.exclude(key_skills=None).values('key_skills', 'published_at')
    skills_by_year = {}
    for skill in all_skills:
        year = skill["published_at"]
        if year not in skills_by_year.keys():
            skills_by_year[year] = list(set(skill["key_skills"].split('\n')))
        else:
            skills_by_year[year].extend(skill["key_skills"].split('\n'))

    for year, skills in skills_by_year.items():
        c = Counter(skills)
        skills_by_year[year] = [(name, c[name] / len(skills) * 100.0) for name, count in c.most_common(10)]
    data = {
        "skills_by_year": dict(sorted(skills_by_year.items(), reverse=True))
    }
    return render(request, 'vacancy/skills_load.html', data)


def last_vacancies(request):
    MAX_COUNT = 10
    vacancies = []
    if request.method == "POST":
        received_form = HHForm(request.POST)
        if received_form.is_valid():
            date = received_form.cleaned_data.get('date')
            vacancies = HHFinder(date, MAX_COUNT).vacancies.to_dict(orient='records')
    data = {
        'vacancies': vacancies,
        'form': HHForm()
    }
    return render(request, 'vacancy/last_vacancies.html', data)
