from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    print(price)
    btn = browser.find_element(By.CSS_SELECTOR, "#book").click()
    browser.execute_script("window.scrollBy(0, 300);")

    x=browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x=int(x)
    result=math.log(abs(12 * math.sin(int(x))))
    print(x, result)
    inp=browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)
    sub=browser.find_element(By.CSS_SELECTOR, "#solve").click()


    alert = browser.switch_to.alert
    print(alert.text)

finally:
    time.sleep(7)
    browser.quit()