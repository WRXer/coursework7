Проект по джанго:  бэкенд-часть SPA веб-приложения.


Установка и настройка
Клонируете репозиторий.

Вариант А:

1. Установите зависимости: pip install -r requirements.txt

2. Примените миграции: python manage.py migrate

3. Перейдите в раздел config/settings.py , найстройте там вашу бд

4. Создайте бд. Далее в файле 4 пункта, найдите раздел DATABASES, введите ваши данные

5. Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.
 Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

6. Создайте файл .env и пропишите все данные из .env.sample

7. Запустите сервер разработки: python manage.py runserver

8. Для работы тг бота на отправку Вам уведомлений вы должны пройти в этого бота и прожать /start

Вариант Б:

1. Клоунируете проект git clone <url>

2. Создайте файл .env и пропишите все данные из .env.sample

3. В терминале прописываете docker-compose build

4. docker-compose up

Приятного пользования
