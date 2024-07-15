from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новину'
        verbose_name_plural = 'Новини'
