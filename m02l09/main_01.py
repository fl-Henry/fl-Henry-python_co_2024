import requests
from fake_headers import Headers

# Создаем объект сессии
session = requests.Session()

session.headers.update(Headers().generate())

# Выполняем запрос с использованием сессии
response = session.get('https://rfspager.app/pager')

# Выводим содержимое ответа
print(session.headers)
print(session.cookies.get_dict())
url = 'https://rfspager.app/livewire/message/pager.feed'
data = {
    "fingerprint": {
        "id": "9mxiojWKqKYG5gz12nXC",
        "name": "pager.feed", "locale": "en", "path": "pager", "method": "GET", "v": "acj"},
    "updates": [{"type": "callMethod", "payload": {"id": "vpzt", "method": "$refresh", "params": []}}]
}
response = session.post(url, data=data)
print(response.status_code)
print(response.text)