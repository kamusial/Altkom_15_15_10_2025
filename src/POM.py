from selenium import webdriver
from time import sleep

class LoginPage:
    def __init__(self, my_driver):
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'
        self.driver = my_driver

    def open(self):
        self.driver.get('https://www.saucedemo.com/v1/')
        sleep(1)
        print(f'Tytuł: {self.driver.title}')

    def close(self):
        self.driver.quit()
        print('Strona zamknięta')

    def enter_username(self, username):
        field = self.driver.find_element('id', self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element('id', self.login_button_name)
        button.click()

    def page_info(self):
        print(f'Adres strony: {self.driver.current_url}')
        print(f'Nazwa strony: {self.driver.name}')
        print(f'Tytuł strony: {self.driver.title}')