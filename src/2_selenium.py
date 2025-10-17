from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from time import sleep
import datetime

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime('Screen_%H%M%S.png')
    window.get_screenshot_as_file('screens\\'+filename)

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/v1/')
sleep(2)
input()
try:
    username_field = driver.find_element(By.CSS_SELECTOR, "[data-test='username']")
except NoSuchElementException:
    print('Nie znaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise

username_field.clear()
username_field.send_keys('standard_user')
# driver.find_element(By.ID, 'user-name').send_keys('standard_user')
sleep(2)
password_field = driver.find_element(By.NAME, 'password')
username_field.clear()
password_field.send_keys('secret_sauce')
sleep(2)
login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/form/input[3]')
#//*[@id="login-button"]
# /html/body/div[2]/div[1]/div/div/form/input[3]

if not login_button.get_attribute("disabled"):
    login_button.click()
    sleep(2)
else:
    print('Nie da się kliknąć')

make_screenshot(driver)
driver.quit()