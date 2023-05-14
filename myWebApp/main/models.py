from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    fio = models.CharField('ФИО', max_length=50)
    group = models.CharField('Группа', max_length=50)
    title = models.TextField('Описание')

    def __str__(self):
        return f'Студент {self.group} группы - {self.fio}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

