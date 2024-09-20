import requests
from bs4 import BeautifulSoup


# # response = requests.get('https://ifconfig.me')
# response = requests.get('https://rfspager.app/')
# print(response.status_code)  # Статус-код ответа
# print(response.text)         # Содержимое ответа
#
# html_doc = "<html><head><title>Title</title></head><body><p>Paragraph</p>bodytext</body></html>"
# soup = BeautifulSoup(html_doc, 'lxml')

# title_tag = soup.title
# print(title_tag)  # <title>Title</title>
# print(title_tag.text)  # <title>Title</title>
# print()

# p_tag = soup.find('body')
# print(p_tag)  # <p>Paragraph</p>
# print(p_tag.text)  # <p>Paragraph</p>
# print(p_tag.contents)  # <p>Paragraph</p>
# for i in p_tag.contents:
#     print(i.text)

# body_tag = soup.find('body')
# print(body_tag)
# child_tag = body_tag.find('p')
# print(child_tag)
# print(child_tag.text)

# response = requests.get('https://rfspager.app/')
# soup = BeautifulSoup(response.text, 'lxml')
#
# img_css = 'img[src]'
# img_tags = soup.select(img_css)
# # img_tags = soup.select_one(img_css)
# print(len(img_tags))
# for tag in img_tags:
#     print(tag['src'])
#     # print(tag['href'])



from fake_headers import Headers
# ctrl + b
import json

# class Test(Headers):
#     def __init__(self):
#         super().__init__()
#

# Создание объекта Headers
headers = Headers()

# Генерация случайных заголовков
fake_headers = headers.generate()
# print(json.dumps(fake_headers, indent=4))


import requests

url = 'https://example.com/api/resource'
data = {"fingerprint":{"id":"9mxiojWKqKYG5gz12nXC","name":"pager.feed","locale":"en","path":"pager","method":"GET","v":"acj"},"serverMemo":{"children":[],"errors":[],"htmlHash":"3062acd5","data":{"numResults":100},"dataMeta":[],"checksum":"4ada08e453279241b67d624d57f2aa5fdda33d5ee2b7608802c2f035a466ed1d"},"updates":[{"type":"callMethod","payload":{"id":"px92","method":"$refresh","params":[]}}]}
request_headers = fake_headers
request_headers.update({
    "Content-Type": "application/json"
})

# Отправка POST-запроса с данными в формате JSON
response = requests.post(url, json=data, headers=request_headers)  # , params=...