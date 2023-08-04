from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", 'telegram_username']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'telegram_username']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            telegram_username=self.validated_data['telegram_username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user