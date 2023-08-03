from rest_framework import serializers

from main.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit

        fields = ['time', 'action', 'place','pleasant_habit','related_habit','periodicity','reward','time_to_complete','public']

