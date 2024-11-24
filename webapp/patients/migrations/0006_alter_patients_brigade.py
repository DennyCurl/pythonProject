# Generated by Django 5.0.7 on 2024-09-18 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_brigades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='brigade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patients.brigades'),
        ),
    ]