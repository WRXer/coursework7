from django import forms
from main.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'