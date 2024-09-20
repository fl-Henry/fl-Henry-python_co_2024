# from selenium import webdriver
#
# # Инициализация WebDriver
# driver = webdriver.Chrome()
#
# # Открытие веб-страницы
# driver.get('https://rfspager.app/pager')
#
# # Получение всех cookies
# cookies = driver.get_cookies()
# cookies1 = [x for x in cookies]
#
# driver.delete_cookie('XSRF-TOKEN')
#
# # Получение всех cookies
# cookies = driver.get_cookies()
# cookies2 = [x for x in cookies]
#
# driver.delete_all_cookies()
#
# # Получение всех cookies
# cookies = driver.get_cookies()
# cookies3 = [x for x in cookies]
#
#
# print(len(cookies1), cookies1)
# print(len(cookies2), cookies2)
# print(len(cookies3), cookies3)


import pickle
from selenium import webdriver

# Инициализация WebDriver
driver = webdriver.Chrome()

# # Сохранение cookies в файл
# cookies = driver.get_cookies()
# with open('cookies.pkl', 'wb') as file:
#     pickle.dump(cookies, file)

print("cookies: ", [x for x in driver.get_cookies()])

# Открытие веб-страницы
driver.get('https://rfspager.app/pager')

# Загрузка cookies из файла
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

print("cookies: ", [x for x in driver.get_cookies()])

driver.refresh()
