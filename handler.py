import os
import json
import requests

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

FUNC_RESPONSE = {'statusCode': 200, 'body': ''}


def send_message(text, message):
    """Отправка сообщения пользователю Telegram."""
    message_id = message['message_id']
    chat_id = message['chat']['id']
    reply_message = {'chat_id': chat_id,
                     'text': text,
                     'reply_to_message_id': message_id}
    requests.post(url=f'{TELEGRAM_API_URL}/sendMessage', json=reply_message)


def handler(event, context):
    update = json.loads(event['body'])
    if 'message' not in update:
        return FUNC_RESPONSE
    message_in = update['message']
    send_message("hey, ley, la la ley", message_in)

    return FUNC_RESPONSE
