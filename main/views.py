from django.shortcuts import render
from rest_framework import generics

from main.models import Habit
from main.serializers import HabitSerializer


# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт по созданию привычки
    """
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """
    Эндпоинт по просмотру привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт по просмотру привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт по обновлению привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт по удалению привычки
    """
    serializer_class = HabitSerializer

