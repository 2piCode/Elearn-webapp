from django.db import models


class Vacancy(models.Model):
    name = models.CharField('Название', blank=False, null=False, max_length=50)
    key_skills = models.TextField('Навыки', blank=True, null=True, default='')
    salary = models.FloatField('Зарплата')
    area_name = models.CharField('Город', max_length=100)
    published_at = models.TextField('Год публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'