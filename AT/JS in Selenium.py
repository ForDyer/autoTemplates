from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    xt = browser.find_element(By.ID, "input_value")
    x = int(xt.text)
    answer = math.log(abs(12 * math.sin(x)))

    fld = browser.find_element(By.ID, "answer")
    fld.send_keys(answer)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
