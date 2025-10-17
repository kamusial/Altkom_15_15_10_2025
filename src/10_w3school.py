from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
sleep(1)

try:
    driver.find_element(By.ID, 'accept-choices').click()
except:
    pass

menu = driver.find_element('id', 'navbtn_tutorials')
HTMLtutorial = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')

try:
    driver.find_element(By.ID, 'accept-choices').click()
except:
    pass

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
sleep(1)

try:
    driver.find_element(By.ID, 'accept-choices').click()
except:
    pass

HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
sleep(1)

tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
tryityourself.click()
sleep(1)

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles

print(currentWindowName)
print(windowNames)

for window in windowNames:
    if window != currentWindowName:
        driver.switch_to.window(window)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))

firstName = driver.find_element(By.ID, 'fname')
firstName.send_keys('Kamil')
