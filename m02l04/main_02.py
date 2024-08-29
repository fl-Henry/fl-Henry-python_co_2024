import json

import requests
from fake_headers import Headers

# Создание объекта Headers
headers = Headers()

# Генерация случайных заголовков
fake_headers = headers.generate()

# print(json.dumps(fake_headers, indent=4))
# # url = 'https://rfspager.app/pager'
#
# # Выполнение запроса с поддельными заголовками
# url = 'https://rfspager.app/pager'
# params = {
#     'id': 'c69d0f2801c01fcf8166',
#     'page': 10
# }
# response = requests.get(url, headers=fake_headers, params=params)
#
# # https://rfspager.app/livewire/livewire.js?id=c69d0f2801c01fcf8166&page=10
#
# # Вывод ответа
# print(response.status_code)
# print(response.text)



# url = 'https://example.com/api/resource'
url = 'https://rfspager.app/livewire/message/pager.feed'
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

data = {"fingerprint":{"id":"9mxiojWKqKYG5gz12nXC","name":"pager.feed","locale":"en","path":"pager","method":"GET","v":"acj"},"serverMemo":{"children":[],"errors":[],"htmlHash":"3062acd5","data":{"numResults":100},"dataMeta":[],"checksum":"4ada08e453279241b67d624d57f2aa5fdda33d5ee2b7608802c2f035a466ed1d"},"updates":[{"type":"callMethod","payload":{"id":"4k4x","method":"$refresh","params":[]}}]}

# Отправка POST-запроса с данными формы
response = requests.post(url, data=data)
