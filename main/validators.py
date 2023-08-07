from datetime import timedelta

from django.core.exceptions import ValidationError



def validate_related_habit_and_reward(value):
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    if value.related_habit and value.reward:
        raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')

class TimeCompleteValidator:
    """
    Время выполнения должно быть не больше 120 секунд.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        min_time = timedelta(seconds=0)
        max_time = timedelta(seconds=120)
        if tmp_val <= min_time:
            raise ValidationError('Напишите продолжительность выполнения')
        if tmp_val > max_time:
            raise ValidationError("Продолжительность не может быть больше 120 секунд.")


class RewardValidator:
    """
    Валидатор вознаграждения
    """
    def __init__(self, field):
        self.field = field

    def __call__(self,data):

        pleasant_habit = data.get('pleasant_habit')
        related_habit = data.get('related_habit')
        reward = data.get('reward')
        if pleasant_habit is False:    #При отсутствии связанной привычки(вознаграждения), необходимо указать вознаграждение(привычку).
            if not related_habit and not reward:
                raise ValidationError('При отсутствии связанной привычки(вознаграждения), необходимо указать вознаграждение(привычку).')
        if related_habit and reward:    #    Исключить одновременный выбор связанной привычки и указания вознаграждения.
            raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')
        if pleasant_habit is True:    #У приятной привычки не может быть вознаграждения или связанной привычки.
            if reward or related_habit:
                raise ValidationError('Приятные привычки могут быть только без вознаграждения и приятной привычки')


class PeriodicityValidator:
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')