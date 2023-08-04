from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Habit
from main.pagination import HabitPaginator
from main.permissions import IsCreatorOrStaff
from main.serializers import HabitSerializer, HabitCreateSerializer



# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт по созданию привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)



class HabitListAPIView(generics.ListAPIView):
    """
    Эндпоинт по просмотру привычек
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        print(user)
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


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт по удалению привычки
    """
    serializer_class = HabitSerializer


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Эндпоинт по публичным привычкам
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
