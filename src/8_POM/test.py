from POM import LoginPage
from selenium import webdriver
from time import sleep
from stary_kod import make_screenshot

moje_okno = webdriver.Chrome()
strona = LoginPage(moje_okno)

strona.open()
sleep(1)
strona.enter_username('standard_user')
strona.enter_password('secret_sauce')

strona.click_login()
sleep(1)
try:
    assert moje_okno.current_url == 'https://www.saucedemo.com/v1/inventory.html', make_screenshot(moje_okno)
except AssertionError:
    print('Asercja nie przeszła')
    raise
else:
    print('Asercja przeszła')
finally:
    print('po asercji')
    strona.close()