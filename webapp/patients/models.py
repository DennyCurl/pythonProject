from django.db import models


class Patients(models.Model):
    last_name = models.CharField('Прізвище')
    first_name = models.CharField("Ім'я")
    middle_name = models.CharField('По батькові')
    birth_date = models.DateField('Дата народження')
    brigade = models.CharField('Бригада')
    address = models.CharField('Адреса проживання')
    begin_sentence = models.DateField('Початок строку')
    end_sentence = models.DateField('Кінець строку')
    term_sentence = models.FloatField('Строк')
    sections = models.FloatField('Статті')
    date_arrival = models.DateField('Дата прибуття')
    date_departure = models.DateField('Дата вибуття')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/patients/{self.id}'

    class Meta:
        verbose_name = 'Пацієнт'
        verbose_name_plural = 'Пацієнти'
