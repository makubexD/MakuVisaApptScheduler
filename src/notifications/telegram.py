import requests
from config import BOT_TOKEN, USER_ID1

def send_notification(msg):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': USER_ID1, 'text': msg}
    requests.post(url, data)