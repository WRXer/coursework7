from datetime import timedelta

from django.core.exceptions import ValidationError

def validate_related_habit_and_reward(value):
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    if value.related_habit and value.reward:
        raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')

def validate_time_to_complete(value):
    """
    Время выполнения должно быть не больше 120 секунд.
    """
    max_time = timedelta(seconds=120)
    if value.time_to_complete is None:
        raise ValidationError('Напишите продолжительность выполнения')
    if value.time_to_complete > max_time:
        raise ValidationError("Продолжительность не может быть больше 120 секунд.")

def validate_reward(value):
    """
    При отсутствии связанной привычки(вознаграждения), необходимо указать вознаграждение(привычку).
    """
    if value.pleasant_habit is False:
        if not value.related_habit and not value.reward:
            raise ValidationError('При отсутствии связанной привычки(вознаграждения), необходимо указать вознаграждение(привычку).')

def validate_habit(value):
    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    if value.pleasant_habit is True:
        if value.reward or value.related_habit:
            raise ValidationError('Приятные привычки могут быть только без вознаграждения и приятной привычки')

def validate_periodicity(value):
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """
    if value.periodicity > 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')