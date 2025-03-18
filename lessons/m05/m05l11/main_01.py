import json

import requests

API_KEY = '7553875249:AAGUo2VpsaaUHnKhkYianL6cnYVyV1EAwK0'

BASE_URL = f'https://api.telegram.org/bot{API_KEY}/'


# # Определяем кнопки
# keyboard = {
#     "inline_keyboard": [
#         [{"text": "Кнопка 1", "callback_data": "1"}, {"text": "Кнопка 2", "callback_data": "2"}]
#     ]
# }

# keyboard = {
#     "keyboard": [
#         [{"text": "Кнопка 1"}, {"text": "Кнопка 2"}],
#         [{"text": "Отправить мое местоположение", "request_location": True}]
#     ],
#     "resize_keyboard": True  # Клавиатура будет адаптироваться под размер экрана
# }

keyboard = {"remove_keyboard": True}

params = {
    'chat_id': 7072349232,
    'text': r'*bold *text\*',
    # 'text': r'',
    'parse_mode': 'MarkdownV2',
    'reply_markup': keyboard,
}

r = requests.post(BASE_URL + 'sendMessage', json=params)
# r = requests.post(BASE_URL + 'getUpdates')
# r = requests.get(BASE_URL + 'sendMessage', params=params)
print(r.url)
print(json.dumps(r.json(), indent=4))
