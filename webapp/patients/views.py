from django.db.models import Q
from .models import Patients
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView


class PatientsListView(ListView):
    model = Patients
    context_object_name = 'patients'

    def get_paginate_by(self, queryset):
        # Отримуємо параметр 'rows' з GET-запиту, якщо він є, або використовуємо значення за замовчуванням
        rows = self.request.GET.get('rows', '15')  # Значення за замовчуванням - 15
        try:
            return int(rows)
        except ValueError:
            # Якщо rows не можна перетворити на ціле число, використовуємо значення за замовчуванням
            return 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Patients.objects.all()
        if query:
            queryset = queryset.filter(
                Q(last_name__icontains=query) |
                Q(first_name__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(birth_date__icontains=query)
            )
        return queryset


class PatientCreateView(CreateView):
    model = Patients
    template_name = 'patients/patient_create.html'
    fields = '__all__'


class PatientUpdateView(UpdateView):
    model = Patients
    fields = '__all__'
    template_name = 'patients/patient_create.html'


class PatientDetailView(DetailView):
    model = Patients
    template_name = 'patients/patient_details.html'
    context_object_name = 'patient'


class PatientDeleteView(DeleteView):
    model = Patients
    success_url = '/patients'
    template_name = 'patients/patient_delete.html'