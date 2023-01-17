import sqlite3 as sql
import pandas as pd

con = sql.connect('db.sqlite3')
vac_name = input('Введите название вакансии: ')

salary_by_year = pd.read_sql("""select STRFTIME() AS 'year', round(avg(salary)) as avg_salary
                        from vacancy_vacancy
                        group by year""", con)
# count_by_year = pd.read_sql("""select STRFTIME('%Y', published_at || '-01') AS 'year',
#                 count(salary) as count
#                         from vacancy_vacancy
#                         group by year """, con)
# salary_by_year_with_vac = pd.read_sql(f"""select STRFTIME('%Y', published_at || '-01') AS 'year',
#                 round(avg(salary)) as avg_salary
#                         from vacancy_vacancy
#                         where name like '%{vac_name}%'
#                         group by year""", con)
# count_by_year_with_vac = pd.read_sql(f"""select STRFTIME('%Y', published_at || '-01') AS 'year',
#                 count(salary) as count
#                         from vacancy_vacancy
#                         where name like '%{vac_name}%'
#                         group by year""", con)
#
# salary_by_city = pd.read_sql("""select area_name, avg from
#                         (select area_name, round(avg(salary)) as avg,
#                          count(salary) as count
#                         from vacancy_vacancy
#                         group by area_name
#                         order by avg desc)
#                     where count > (select count(*) from vacancy_vacancy) * 0.01
#                     limit 10""", con)
# count_by_city = pd.read_sql("""select area_name,
#                         round(cast(count as real) / (select count(*) from vacancy_vacancy) * 100, 2)
#                          as percent from
#                         (select area_name, count(salary) as count
#                         from vacancy_vacancy
#                         group by area_name
#                         order by count desc)
#                         limit 10""", con)
#
print('Динамика уровня зарплат по годам \n', salary_by_year)
# print('Динамика количества вакансий по годам \n', count_by_year)
# print(f'Динамика уровня зарплат по годам для выбранной профессии {vac_name}\n', salary_by_year_with_vac)
# print(f'Динамика количества вакансий по годам для выбранной профессии {vac_name}\n', count_by_year_with_vac)
# print('Уровень зарплат по городам (в порядке убывания) - только первые 10 значений \n', salary_by_city)
# print('Доля вакансий по городам (в порядке убывания) - только первые 10 значений \n', count_by_city)