from django.shortcuts import redirect, render
from .models import Patients
from .forms import PatientsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def patients_home(request):
    patients = Patients.objects.all()
    return render(request, 'patients/patients_home.html', {'patients': patients})


class PatientDetailView(DetailView):
    model = Patients
    template_name = 'patients/patient_details.html'
    context_object_name = 'patient'


class PatientDeleteView(DeleteView):
    model = Patients
    success_url = '/patients'
    template_name = 'patients/patient_delete.html'


class PatientUpdateView(UpdateView):
     model = Patients
     template_name = 'patients/patient_create.html'
     form_class = PatientsForm


def patient_create(request):
    error = ''
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_home')
        else:
            error = 'Форма була невірна'

    form = PatientsForm()

    data = {
        'form': form,
        'error': error}

    return render(request, 'patients/patient_create.html', data)
