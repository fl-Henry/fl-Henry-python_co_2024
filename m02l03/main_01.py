import requests
from bs4 import BeautifulSoup

#
# response = requests.get('https://ifconfig.me')
# print(response.status_code)  # Статус-код ответа
# print(response.text)         # Содержимое ответа



# html_doc = "<html><head><title>Title</title></head><body><p>Paragraph</p>bodytext</body></html>"
# soup = BeautifulSoup(html_doc, 'lxml')
#
# title_tag = soup.body
# print(title_tag)  # <title>Title</title>
#
# print(title_tag.text)  # Title
# print(title_tag.get_text())  # Title
#
# p_tag = soup.find('p')
# print(p_tag)  # <p>Paragraph</p>
# print(p_tag.text)  # <p>Paragraph</p>


url = 'https://rfspager.app/pager'
response = requests.get(url)
print("status_code:", response.status_code)  # 200

soup = BeautifulSoup(response.text, 'lxml')

# all_links = soup.find_all('a', class_='inline-flex')
# all_links = soup.select('a[href*="mailto"]')
# all_links = soup.select('a.inline-flex')

# print(len(all_links))
# for link in all_links:
#     print(link.get('href').strip())

url = 'https://rfspager.app/'
url = 'https://www.thesprucepets.com/about-us-4776796#toc-contact-us/'
response = requests.get(url)
print("status_code:", response.status_code)  # 200
soup = BeautifulSoup(response.text, 'lxml')

# play_store = soup.select_one('a[href*="play.google"]')
play_store = soup.select_one('a[href*="mailto"]')
print(play_store.text)
# print(play_store.get_text())
# print(play_store.contents)
print(play_store.get('href'))
# print(play_store['href'])
# print(play_store.attrs)
# print(play_store.get('href1'))
# print(play_store['href1'])

# img = play_store.find('img')
# print(img)
