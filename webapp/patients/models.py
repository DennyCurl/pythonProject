from django.db import models
from django.urls import reverse


class Brigades(models.Model):
    name = models.CharField('Бригада', max_length=5)

    def __str__(self):
        return f'{self.name}'


class Patients(models.Model):
    last_name = models.CharField('Прізвище', max_length=30)
    first_name = models.CharField("Ім'я", max_length=30)
    middle_name = models.CharField('По батькові', max_length=30)
    birth_date = models.DateField('Дата народження')
    brigade = models.ForeignKey(Brigades, on_delete=models.PROTECT, verbose_name='Бригада')
    address = models.CharField('Адреса проживання', max_length=30)
    begin_sentence = models.DateField('Початок строку')
    end_sentence = models.DateField('Кінець строку',  blank=True, null=True)
    term_sentence = models.DurationField('Строк', null=True)
    sections = models.CharField('Статті', max_length=30)
    date_arrival = models.DateField('Дата прибуття')
    date_departure = models.DateField('Дата вибуття',  blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} {self.birth_date}"

    def get_absolute_url(self):
        return reverse('patient_details', args=[str(self.id)])

    class Meta:
        verbose_name = 'Пацієнт'
        verbose_name_plural = 'Пацієнти'
        ordering = ['last_name']
        indexes = [
            models.Index(fields=['last_name', 'first_name', 'middle_name', 'birth_date'])
        ]
