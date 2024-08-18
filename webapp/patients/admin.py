from django.contrib import admin

from .models import Patients


class PatientsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'birth_date')
    list_filter = ('brigade', 'date_arrival')


admin.site.register(Patients, PatientsAdmin)
