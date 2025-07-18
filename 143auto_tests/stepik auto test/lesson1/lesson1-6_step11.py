from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys('Иван')
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block>.form-group.third_class input")
    input3.send_keys('моя почта - секрет фирмы))')
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.form-group.second_class input")
    input2.send_keys('Васильевич')
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except:
    print("Есть ошибка в форме")

finally:
    time.sleep(3)
    browser.quit()

