from sys import executable

from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://google.com')
sleep(2)
print(f'tytuł strony: {driver.title}')
print(f'nazwa strony: {driver.name}')
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
sleep(2)
search_field = driver.find_element('id', 'APjFqb')
search_field.send_keys('Dokąd nocą tupta jeż?')
sleep(2)
# search_button = driver.find_element('name', 'btnK')
# search_button.click()
search_field.send_keys(Keys.ENTER)
input('Czekam na enter')


driver.quit()
print('koniec')