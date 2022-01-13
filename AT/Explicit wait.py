from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    prc = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    btn = browser.find_element(By.ID, "book")
    btn.click()

    x1 = browser.find_element(By.ID, "input_value")
    x = int(x1.text)
    answr = math.log(abs(12 * math.sin(x)))

    fld = browser.find_element(By.ID, "answer")
    fld.send_keys(answr)

    sbmt = browser.find_element(By.ID, "solve")
    sbmt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()