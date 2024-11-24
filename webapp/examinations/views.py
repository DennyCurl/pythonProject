from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView, ListView
from .models import Examinations
from .forms import ExaminationForm
from patients.models import Patients
from django.urls import reverse_lazy


class PatientExaminationsView(ListView):
    model = Examinations
    template_name = 'examinations.html'
    context_object_name = 'examinations'

    def get_queryset(self):
        # Отримуємо пацієнта за ID
        patient = get_object_or_404(Patients, id=self.kwargs['patient_id'])

        # Повертаємо всі огляди для цього пацієнта
        return Examinations.objects.filter(patient=patient)

    def get_context_data(self, **kwargs):
        # Отримуємо контекст для шаблону
        context = super().get_context_data(**kwargs)

        # Додаємо пацієнта до контексту для відображення в шаблоні
        patient = get_object_or_404(Patients, id=self.kwargs['patient_id'])
        context['patient'] = patient

        return context


class ExaminationCreateView(CreateView):
    model = Examinations
    template_name = 'examination_create.html'
    form_class = ExaminationForm

    def get_initial(self):
        # Отримуємо пацієнта за ID з URL
        patient = get_object_or_404(Patients, pk=self.kwargs['patient_id'])
        # Встановлюємо пацієнта за замовчуванням у формі
        return {'patient': patient}

    def form_valid(self, form):
        # Встановлюємо пацієнта безпосередньо при збереженні, якщо він не був переданий
        form.instance.patient = get_object_or_404(Patients, pk=self.kwargs['patient_id'])
        return super().form_valid(form)

    def get_success_url(self):
        # Переходимо назад до списку оглядів для пацієнта
        return reverse_lazy('examinations', kwargs={'patient_id': self.kwargs['patient_id']})


class ExaminationUpdateView(UpdateView):
    model = Examinations
    fields = '__all__'
    template_name = 'examination_create.html'


class ExaminationDetailView(DetailView):
    model = Examinations
    template_name = 'examination_details.html'


class ExaminationDeleteView(DeleteView):
    model = Examinations
    success_url = 'examinations'
    template_name = 'examination_delete.html'
