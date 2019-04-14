from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

opt = webdriver.ChromeOptions()

opt.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opt)

# Переходим на яндекс
driver.get('https://yandex.ru')
driver.implicitly_wait(5)

#Ищем строку поиска, вводим
search = driver.find_element_by_xpath("//*[@class='input__control input__input']")
search.send_keys('Тензор tensor.ru')

#Проверяем таблицу с подсказками
suggest = driver.find_element_by_xpath("//*[@class='suggest2__content suggest2__content_theme_normal']")

# Нажимаем ENTER
search.send_keys(Keys.ENTER)

# Проверяем, что результаты поиска есть
results = driver.find_element_by_xpath("//*[contains(@class, 'serp-list serp-list_left_yes')]")

# Проверяем, что первая ссылка - сайт Тензора
first_result = driver.find_element_by_xpath("//*[@class = 'serp-item'][1]//*[@href='https://tensor.ru/']")

driver.close()
