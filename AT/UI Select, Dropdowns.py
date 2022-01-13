from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    x1 = int(x.text)
    x2 = int(y.text)
    total = x1 + x2
    answer = str(total)

    dd = Select(browser.find_element(By.ID, "dropdown"))
    dd.select_by_value(answer)

    sbmt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sbmt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
