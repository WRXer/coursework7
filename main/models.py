from django.db import models
from django.conf import settings
from django.utils import timezone

import datetime


# Create your models here.
NULLABLE = {'blank': True, 'null': True}

class Habit(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="создатель привычки", related_name='habits_creator')
    place = models.CharField(max_length=100, verbose_name="место выполнения")    #место
    send_time = models.TimeField(verbose_name='время отправки уведомления', default=datetime.time(8, 0))
    send_date = models.DateField(verbose_name="дата выполнения", default=timezone.now)
    time = models.TimeField(verbose_name="время выполнения")   #время,когда выполнять
    action = models.CharField(max_length=200, verbose_name="действие")   #действие
    pleasant_habit = models.BooleanField(default=False, verbose_name="признак положительной привычки")     #признак положительной привычки
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,limit_choices_to={'pleasant_habit': True}, verbose_name="связанная привычка")     #связанная привычка
    periodicity = models.PositiveIntegerField(default=1, verbose_name="периодичность")    #периодичность каждый день
    reward = models.CharField(max_length=200, verbose_name="вознаграждение", blank=True, null=True)   #вознаграждение
    time_to_complete = models.DurationField(verbose_name="время на выполнение")   #время на выполнение
    public = models.BooleanField(default=False)     #признак публичности(общий доступ)

    def __str__(self):
        return self.action


    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = 'привычки'