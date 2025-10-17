from POM import LoginPage
from selenium import webdriver
from time import sleep
from stary_kod import make_screenshot
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/v1/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/v1/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/v1/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/v1/inventory.html')
]

@pytest.mark.skip
@pytest.mark.parametrize('username, passwd, url', test_data)
def test_login_page(username, passwd, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    sleep(1)
    page.enter_username(username)
    page.enter_password(passwd)
    page.click_login()
    sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver)
    except AssertionError:
        print('Asercja nie przeszła')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print('po asercji')
        page.close()


@pytest.mark.skipif(len('piesek') == 5, reason='Not implemented')
def test2():
    assert 2 == 2

@pytest.mark.xfail(reason='nie nasz dzal')
def test3():
    assert 3 == 3

import sys

if sys.platform.startswith("win"):
    @pytest.mark.skip("skipping linux-only tests")
    def test_default():
        assert 3 == 4