import requests
from bs4 import BeautifulSoup



# response = requests.get('https://ifconfig.me')
# print(response.status_code)  # Статус-код ответа
# print(response.text)         # Содержимое ответа

# html_doc = "<html><head><title>Title</title></head><body><p>Paragraph</p><p><p>Paragraph3</p>Paragraph2</p>bodytext</body></html>"
# soup = BeautifulSoup(html_doc, 'lxml')

url = 'https://rfspager.app/pager'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# title_text = soup.title.text
# print(title_text)  # Title
# print(soup.title.get_text())  # Title

# print(soup.prettify())
# print(soup.body.text)  # Title
# print(soup.body.get_text())  # Title
# print(soup.body.contents)  # Title

# print(soup.prettify())
# print(soup.find('a'))
# print(soup.find_all('a'))

# all_links = soup.find_all('a', target="_self")
# print(len(all_links))
# print(all_links)

all_elems = soup.select('table thead.uppercase th')
# one_elem = soup.select_one('table thead.uppercase th')
#
# print(one_elem)
print(len(all_elems))

all_headers = [x.text for x in all_elems]
print(all_headers)
all_classes = [x['class'] for x in all_elems]
all_scope = [x.get('scope') for x in all_elems]
print(all_classes)
print(all_scope)