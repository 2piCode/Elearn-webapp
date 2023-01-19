from datetime import timedelta
import json
import time
import requests

import pandas as pd
from math import ceil
from bs4 import BeautifulSoup


class HHFinder:
    def __init__(self, date, max_count):
        self.date_from = date
        self.date_to = date + timedelta(days=1)
        self.max_count = max_count
        df = self.get_vacancies()
        self.vacancies = (df
                          .assign(published_at=df["published_at"].astype('datetime64'),
                                  salary_from=df[["salary_from", "salary_to"]]
                                  .mean(axis=1).astype('int32'))
                          .rename({"salary_from": "salary"}, axis="columns")
                          .drop(columns=["salary_currency", "salary_to"])
                          .sort_values(by=['published_at'], ascending=True)
                          )[:max_count]

    def get_vacancies(self, per_page=100, pages=20):
        df = pd.DataFrame(columns=["name", "description", "key_skills", "salary_from", "salary_to", "salary_currency",
                                   "company", "area_name", "published_at"])

        parsing_iterations = 100
        delta_time = self.date_to - self.date_from
        n_hours = delta_time.days * 24 + delta_time.seconds / 3600
        time_chunk = ceil(n_hours / parsing_iterations)
        time_from = self.date_from.replace(second=0, microsecond=0)

        for iteration in range(parsing_iterations):
            time_to = time_from + timedelta(hours=time_chunk)

            if time_to > self.date_to or df.shape[0] >= self.max_count:
                break

            for page in range(pages):
                vacancy_filter = {
                    'text': 'C++-разработчик OR C++-developer OR C++ OR c++',
                    'search_field': "name",
                    'per_page': per_page,
                    'page': page,
                    'specialization': 1,
                    'date_from': time_from.isoformat(),
                    'date_to': time_to.isoformat(),
                    'only_with_salary': True,
                    'currency': 'RUR'
                }

                vacancies_page = get_page(vacancy_filter)
                if page == vacancies_page["pages"]:
                    break

                frame = get_fields(vacancies_page)
                df = pd.concat([df, frame], ignore_index=True)
                time.sleep(0.1)

            time_from = time_to
        return df


def get_page(vacancy_filter, id=''):
    req = requests.get('https://api.hh.ru/vacancies/' + id, vacancy_filter)
    data = req.content.decode()
    return json.loads(data)


def get_fields(data):
    parsed_relevant_vacancies_fields = [get_relevant_vacancy_fields(values) for values in data["items"]]

    frame = pd.DataFrame(parsed_relevant_vacancies_fields,
                         columns=["name", "description", "key_skills", "salary_from", "salary_to", "salary_currency",
                                  "company", "area_name",
                                  "published_at"])
    return frame


def get_relevant_vacancy_fields(data):
    info = get_page({}, data['id'])

    name = data["name"]

    temp_description = info["description"]
    soup = BeautifulSoup(temp_description, 'html.parser')
    description = soup.get_text()

    key_skills = ", ".join([s for d in info["key_skills"] for s in d.values()])

    company = data["employer"]["name"]
    area_name = data["area"]["name"]
    published_at = data["published_at"]

    salary = data["salary"]
    if salary is None:
        salary_from = None
        salary_to = None
        salary_currency = None
    else:
        salary_from = salary["from"]
        salary_to = salary["to"]
        salary_currency = salary["currency"]
    return [name, description, key_skills, salary_from, salary_to, salary_currency, company, area_name, published_at]
