from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    treasure = browser.find_element(By.ID, "treasure")
    x = int(treasure.get_attribute("valuex"))
    result = math.log(abs(12 * math.sin(x)))

    text = browser.find_element(By.ID, "answer")
    text.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    sbmt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sbmt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
