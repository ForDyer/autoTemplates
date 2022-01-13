from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:

    browser = webdriver.Chrome()
    link = ""
    browser.get(link)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()