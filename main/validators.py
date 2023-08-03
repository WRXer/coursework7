from django.core.exceptions import ValidationError

def validate_related_habit_and_reward(value):
    if value.related_habit and value.reward:
        raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')