# Preferred selector order: id > name > css > xpath
import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла