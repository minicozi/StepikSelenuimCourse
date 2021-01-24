import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

    # говорим Selenium проверять в течение 15 секунд, пока поле не будет содержать значение "$100"
    WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    browser.find_element_by_css_selector("#book").click()

    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    answer_element = browser.find_element_by_css_selector("#answer")
    answer_element.send_keys(y)

    submit_button = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
