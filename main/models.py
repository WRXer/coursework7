from django.db import models
from django.conf import settings


# Create your models here.


class Habit(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits_created')
    place = models.CharField(max_length=100)    #место
    time = models.TimeField()   #время,когда выполнять
    action = models.CharField(max_length=200)   #действие
    pleasant_habit = models.BooleanField(default=False)     #признак положительной привычки
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)     #связанная привычка
    periodicity = models.PositiveIntegerField(default=1)    #периодичность
    reward = models.CharField(max_length=200)   #вознаграждение
    time_to_complete = models.DurationField()   #время на выполнение
    public = models.BooleanField(default=False)     #признак публичности(общий доступ)

    def __str__(self):
        return f"{self.creator} - {self.action}"