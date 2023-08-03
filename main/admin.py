from django.contrib import admin

from main.models import Habit


# Register your models here.

@admin.register(Habit)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("creator", 'time', 'action', 'place','pleasant_habit','related_habit','periodicity','reward','time_to_complete','public')
