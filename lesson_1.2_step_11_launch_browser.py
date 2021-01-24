import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
#webdriverChromeOptions.binary_location = "C:\\Users\\sergm\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"

# Open the browser
driver = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

input("Press Enter to continue...")

textArea = driver.find_element_by_css_selector(".textarea")                 # Ищем поле для ввода текста
textArea.send_keys("get()")                                                 # Напишем текст ответа в найденное поле
time.sleep(5)
submitButton = driver.find_element_by_css_selector(".submit-submission")    # Найдем кнопку, которая отправляет введенное решение
submitButton.click()
time.sleep(5)

driver.quit()
