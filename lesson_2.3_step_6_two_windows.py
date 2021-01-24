import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    browser.get(link)

    # Работа с модальным окном
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])

    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    answer_element = browser.find_element_by_css_selector("#answer")
    answer_element.send_keys(y)

    submit_button = browser.find_element_by_css_selector(".btn.btn-primary")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
