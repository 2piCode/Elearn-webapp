# Generated by Django 4.1.5 on 2023-01-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('key_skills', models.TextField(blank=True, default='', null=True, verbose_name='Навыки')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('area_name', models.CharField(max_length=100, verbose_name='Город')),
                ('published_at', models.TextField(verbose_name='Год публикации')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]