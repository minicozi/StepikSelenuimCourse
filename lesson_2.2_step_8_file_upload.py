import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

webdriverChromeOptions: Options = webdriver.ChromeOptions()
webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input[name='firstname']")
    first_name.send_keys("Test")
    last_name = browser.find_element_by_css_selector("input[name='lastname']")
    last_name.send_keys("Test")
    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys("test@test.tst")

    # Работа с файлом
    with open("sample.txt", "w") as file:
        content = file.write("Sample text.")                    # create a file
        file.close()
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'sample.txt')         # добавляем к этому пути имя файла

    # Работа с <input type='file'/>
    file_upload_button = browser.find_element_by_css_selector("#file")
    file_upload_button.send_keys(file_path)                     # send_keys умеет грузить файлы, если <input> нужного типа

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:

    os.remove("sample.txt")

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
