from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", 'telegram_username']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['email', 'password', 'telegram_username']

    #def save(self, *args, **kwargs):
    #    user = User(
    #        email=self.validated_data['email'],
    #        telegram_username=self.validated_data['telegram_username']
    #    )
    #    password = self.validated_data['password']
    #    user.set_password(password)
    #    user.save()
    #    return user