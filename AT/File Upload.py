from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    fname = browser.find_element(By.NAME, "firstname")
    fname.send_keys("Test")

    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Test")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("test@gmail.com")

    fs = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload.txt')
    fs.send_keys(file_path)

    sbmt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sbmt.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()