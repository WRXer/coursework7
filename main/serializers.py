from rest_framework import serializers

from main.models import Habit
from main.validators import TimeCompleteValidator, RewardValidator, PeriodicityValidator
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'creator', 'action', 'place']
        #fields = ['time', 'action', 'place','pleasant_habit','related_habit','periodicity','reward','time_to_complete','public']


class HabitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ['id', 'time', 'action', 'place','pleasant_habit','related_habit','periodicity','reward','time_to_complete','public']
        validators = [TimeCompleteValidator(field='time_to_complete'),
                      RewardValidator(field='reward'),
                      PeriodicityValidator(field='periodicity')
                      ]

    def create(self, validated_data):
        user = self.context['request'].user
        habit = Habit.objects.create(creator=user, **validated_data)
        return habit