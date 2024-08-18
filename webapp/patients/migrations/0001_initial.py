# Generated by Django 5.0.7 on 2024-08-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Прізвище')),
                ('first_name', models.CharField(max_length=30, verbose_name="Ім'я")),
                ('middle_name', models.CharField(max_length=30, verbose_name='По батькові')),
                ('birth_date', models.DateField(verbose_name='Дата народження')),
                ('brigade', models.CharField(max_length=5, verbose_name='Бригада')),
                ('address', models.CharField(max_length=30, verbose_name='Адреса проживання')),
                ('begin_sentence', models.DateField(verbose_name='Початок строку')),
                ('end_sentence', models.DateField(verbose_name='Кінець строку')),
                ('term_sentence', models.FloatField(verbose_name='Строк')),
                ('sections', models.FloatField(max_length=30, verbose_name='Статті')),
                ('date_arrival', models.DateField(verbose_name='Дата прибуття')),
                ('date_departure', models.DateField(verbose_name='Дата вибуття')),
            ],
            options={
                'verbose_name': 'Пацієнт',
                'verbose_name_plural': 'Пацієнти',
            },
        ),
    ]
