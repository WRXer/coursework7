from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.permissions import IsOwnerOrSuperuser
from users.serializers import UserSerializer, UserCreateSerializer


# Create your views here.
class UserListView(generics.ListAPIView):
    """
    Эндпоинт вывода всех пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = User.objects.all()
        return queryset


class UserDetailView(generics.RetrieveAPIView):
    """
    Эндпоинт детализации пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrSuperuser]


class UserUpdateView(generics.UpdateAPIView):
    """
    Эндпоинт обновления данных пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrSuperuser]


class UserDeleteView(generics.DestroyAPIView):
    """
    Эндпоинт удаления аккаунта
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrSuperuser]


class UserCreateView(generics.CreateAPIView):
    """
    Эндпоинт создания аккаунта
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)