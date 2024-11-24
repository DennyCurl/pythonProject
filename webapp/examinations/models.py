from django.db import models
from django.urls import reverse
from patients.models import Patients


class Examinations(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='examinations', verbose_name="Пацієнт")
    date = models.DateField('Дата огляду', auto_now_add=True)
    doctor_name = models.CharField("Ім'я лікаря", max_length=50)
    complaints = models.TextField('Скарги', blank=True, null=True)
    diagnosis = models.TextField('Діагноз', blank=True, null=True)
    treatment = models.TextField('Призначення', blank=True, null=True)

    class Meta:
        verbose_name = "Медичний огляд"
        verbose_name_plural = "Медичні огляди"

    def __str__(self):
        return f"Огляд пацієнта {self.patient.last_name} від {self.date}"

    def get_absolute_url(self):
        return reverse('examination_details', args=[str(self.id)])