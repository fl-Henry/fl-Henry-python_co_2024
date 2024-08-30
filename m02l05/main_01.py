import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument('--headless')  # Запуск в фоновом режиме
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Firefox()

url = 'https://rfspager.app/pager'
driver.get(url)
print(driver.title)  # Должен вывести "Google"
time.sleep(5)

elements = driver.find_elements(By.CSS_SELECTOR, 'thead th')
print(len(elements))
print([x.text for x in elements])
# element = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
# element.click()
time.sleep(10)

current_url = driver.current_url
print(current_url)


# url = 'https://rfspager.app/login'
# driver.get(url)
#
# # input[name="email"]
# email = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
# email.send_keys('kasfdjhals@gmail.com')
#
# # input[name="password"]
# password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
# password.send_keys('sdlkfjhglskdfg')
#
# time.sleep(10)

driver.quit()