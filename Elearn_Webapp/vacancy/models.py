from django.db import models


class Vacancy(models.Model):
    name = models.CharField('Название', max_length=50)
    key_skills = models.TextField("Навыки")
    salary_from = models.FloatField('Нижняя граница зарплаты')
    salary_to = models.FloatField('Верхняя граница зарплаты')
    salary_currency = models.CharField('Валюта оклада', max_length=10)
    area_name = models.CharField('Город', max_length=100)
    published_at = models.DateTimeField('Время публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'