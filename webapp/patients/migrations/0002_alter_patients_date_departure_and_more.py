# Generated by Django 5.0.7 on 2024-08-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date_departure',
            field=models.DateField(blank=True, verbose_name='Дата вибуття'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='end_sentence',
            field=models.DateField(blank=True, verbose_name='Кінець строку'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sections',
            field=models.CharField(max_length=30, verbose_name='Статті'),
        ),
    ]