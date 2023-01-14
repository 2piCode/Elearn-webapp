import sqlite3 as sql
import pandas as pd

connection = sql.connect('db.sqlite3')
df = pd.read_csv("vacancies_with_skills.csv", verbose=True, low_memory=False)
df = (
    df.to_sql("vacancy_vacancy", connection, index=True, if_exists="replace")
)