from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Patients
from .forms import PatientsForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView


class PatientsListView(ListView):
    model = Patients
    context_object_name = 'patients'
    paginate_by = 15


class SearchPatients(ListView):
    model = Patients
    context_object_name = 'patients'
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Patients.objects.filter(
            Q(last_name__icontains=query) | Q(first_name__icontains=query) |
            Q(middle_name__icontains=query) | Q(birth_date__icontains=query)
            )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get('q')}&'
        return context


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
    fields = '__all__'
    template_name = 'patients/patient_create.html'
#    form_class = PatientsForm


class PatientCreateView(CreateView):
    model = Patients
    template_name = 'patients/patient_create.html'
    fields = '__all__'
#    form_class = PatientsForm

    # def patient_create(request):
    #     error = ''
    #     if request.method == 'POST':
    #         form = PatientsForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('patients')
    #         else:
    #             error = 'Форма була невірна'

    # form = PatientsForm()
    #
    # data = {
    #     'form': form,
    #     'error': error}
    #
    # return render(request, 'patients/patient_create.html', data)
