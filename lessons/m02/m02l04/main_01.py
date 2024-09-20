import json

import requests
from fake_headers import Headers

# Создание объекта Headers
headers = Headers()

# Генерация случайных заголовков
fake_headers = headers.generate()

print(json.dumps(fake_headers, indent=4))

# response = requests.get("https://whatmyuseragent.com/")
# # python-requests/2.32.3
# print(response.text)

# response = requests.get("https://rfspager.app/pager/", headers=fake_headers)
# # python-requests/2.32.3
# print(response.text)
body = {"fingerprint":{"id":"9mxiojWKqKYG5gz12nXC","name":"pager.feed","locale":"en","path":"pager","method":"GET","v":"acj"},"serverMemo":{"children":[],"errors":[],"htmlHash":"3062acd5","data":{"numResults":100},"dataMeta":[],"checksum":"4ada08e453279241b67d624d57f2aa5fdda33d5ee2b7608802c2f035a466ed1d"},"updates":[{"type":"callMethod","payload":{"id":"3uah","method":"$refresh","params":[]}}]}
body_text = '{"fingerprint":{"id":"9mxiojWKqKYG5gz12nXC","name":"pager.feed","locale":"en","path":"pager","method":"GET","v":"acj"},"serverMemo":{"children":[],"errors":[],"htmlHash":"3062acd5","data":{"numResults":100},"dataMeta":[],"checksum":"4ada08e453279241b67d624d57f2aa5fdda33d5ee2b7608802c2f035a466ed1d"},"updates":[{"type":"callMethod","payload":{"id":"3uah","method":"$refresh","params":[]}}]}'

params = {'id': 'c69d0f2801c01fcf8166', ...}
# d=c69d0f2801c01fcf8166

response = requests.post(
    "https://rfspager.app/pager/",
    data=body_text,
    json=body,
    headers=...,
    params=params
)

print(response.json())  # json.loads()  -> JSON
print(response.text)    # string