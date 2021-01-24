import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    browser.get(link)

    num1 = int(browser.find_element_by_css_selector("#num1").text)
    num2 = int(browser.find_element_by_css_selector("#num2").text)
    str_sum = str(num1 + num2)

    # Работа со списком
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str_sum)

    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
