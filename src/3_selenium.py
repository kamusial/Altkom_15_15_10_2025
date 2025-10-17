from optparse import Option

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, TimeoutException
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime('Screen_%H%M%S.png')
    window.get_screenshot_as_file('screens\\'+filename)

def wait_for_id(element_id):
    timeout = 5
    timeout_message = f'Element {element_id} nie pojawił się w czasie {timeout} sekund.'
    lokalizator = (By.ID, element_id)
    znaleziono = EC.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)
#    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, element_id)), timeout_message)


# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--headless=new")
#
driver = webdriver.Chrome() #options=chrome_options)

driver.get('https://www.saucedemo.com/v1/')
sleep(1)

try:
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.NAME, 'password')
except NoSuchElementException:
    print('Nie znaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise

username_field.clear()
username_field.send_keys('standard_user')
username_field.clear()
password_field.send_keys('secret_sauce')

try:
    login_button = wait_for_id('login-button')
except TimeoutException:
    print('NIe znaleziono')
    raise
else:
    print('Znaleziono')
finally:
    make_screenshot(driver)
    driver.quit()

# if not login_button.get_attribute("disabled"):
#     login_button.click()
#     sleep(2)
# else:
#     print('Nie da się kliknąć')

