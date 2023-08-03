from celery import shared_task
from django.conf import settings
import requests



@shared_task
def check_habit():
    #TOKEN = settings.TELEGRAM_BOT_TOKEN
    #url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    #data = requests.get(url).json()
    #print(data['result'][0]['message']['chat']['id'])

    TOKEN = settings.TELEGRAM_BOT_TOKEN
    chat_id = "527186007"  # 10 знаков, полученных на предыдущем шаге
    message = "Пора выполнить привычку:)))!"
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Сообщение успешно отправлено.")
    else:
        print("Ошибка при отправке сообщения.")