import requests
from fake_headers import Headers

# Создаем объект сессии
session = requests.Session()
session.headers.update(Headers().generate())
# session.proxies.update({'http': ''})
# session.cookies.update({})

# Выполняем запрос с использованием сессии
response = session.get('https://rfspager.app/pager')
# response = session.post('https://rfspager.app/pager')

# Выводим содержимое ответа
# print(response.text)
print(response.status_code)
print(session.cookies.get_dict())