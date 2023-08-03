from django import forms
from main.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        exclude = ['creator']

        #fields = "__all__"