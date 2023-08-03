from datetime import timedelta

from django.core.exceptions import ValidationError

def validate_related_habit_and_reward(value):
    if value.related_habit and value.reward:
        raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')

def validate_time_to_complete(value):
    max_time = timedelta(seconds=120)
    if value.time_to_complete > max_time:
        raise ValidationError("Продолжительность не может быть больше 120 секунд.")

def validate_reward(value):
    if not value.related_habit and not value.reward:
        raise ValidationError('При отсутствии связанной привычки, необходимо указать вознаграждение.')