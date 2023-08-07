from rest_framework import generics, status
from rest_framework.response import Response
from main.models import Habit
from main.pagination import HabitPaginator
from main.permissions import IsCreatorOrStaff, IsOwner
from main.serializers import HabitSerializer, HabitCreateSerializer



# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт по созданию привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Эндпоинт по просмотру привычек
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Habit.objects.all()
        else:
            queryset = Habit.objects.filter(creator=self.request.user)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт по просмотру привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsCreatorOrStaff]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт по обновлению привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsCreatorOrStaff]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт по удалению привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Эндпоинт по публичным привычкам
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        publics = Habit.objects.filter(public=True)
        return publics