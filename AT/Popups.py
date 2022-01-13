from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    conf = browser.switch_to.alert
    conf.accept()

    x1 = browser.find_element(By.ID, "input_value")
    x = int(x1.text)
    answr = math.log(abs(12 * math.sin(x)))

    fld = browser.find_element(By.ID, "answer")
    fld.send_keys(answr)

    sbmt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sbmt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()







