import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    browser.get(link)

    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    answer_element = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    answer_element.send_keys(y)

    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()

    submit_button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
