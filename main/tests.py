from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from main.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        """
        Настройка для тестирования
        """
        self.user = User.objects.create(
            email="test@test.com",
            password="test",
            telegram_username="test",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(creator=self.user, time='15:00:00', action= "test", place= "test", pleasant_habit= False, periodicity= 1,reward= "test",time_to_complete= '00:01:40', public= False)

    def test_create_habit(self):
        data = {
            'creator': self.user,
            "time": "15:00:00",
            "action": "test",
            "place": "test",
            "pleasant_habit": "False",
            "related_habit": "",
            "periodicity": 1,
            "reward": "test",
            "time_to_complete": "00:01:40",
            "public": "False"
        }
        response = self.client.post("/habit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_get_habits(self):
        """
        Тестирование вывода списка привычек
        """
        response = self.client.get(
            reverse('main:habit_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """
        Тестирование обновления привычки
        """
        updata = {
            "action": "testtt_ok",
        }
        update_url = f"/habit/update/{self.habit.id}/"
        response = self.client.patch(update_url, data=updata)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),{'id': self.habit.id, 'creator': self.user.id, 'action': 'testtt_ok', 'place': 'test'} )

    def test_detail_habit(self):
        """
        Тестирование детализации привычки
        """
        response = self.client.get(f'/habit/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_related_habit_and_reward(self):
        """
        Тест на исключить одновременный выбор связанной привычки и указания вознаграждения
        """
        data = {
            'creator': self.user,
            "time": "15:00:00",
            "action": "test",
            "place": "test",
            "pleasant_habit": "False",
            "related_habit": "test",
            "periodicity": 1,
            "reward": "test",
            "time_to_complete": "00:01:40",
            "public": "False"
        }
        response = self.client.post(f'/habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_time_to_complete(self):
        data = {
            'creator': self.user.id,
            "time": "15:00:00",
            "action": "test",
            "place": "test",
            "pleasant_habit": 'False',
            "related_habit": '',
            "periodicity": 1,
            "reward": "test",
            "time_to_complete": '15:00:00',
            "public": 'False'
        }
        response = self.client.post(f'/habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
