# Generated by Django 5.0.7 on 2024-11-24 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_alter_patients_brigade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='brigade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patients.brigades', verbose_name='Бригада'),
        ),
    ]