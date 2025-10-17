def css_for(el):
    tag = el.tag_name
    el_id = el.get_attribute("id")
    if el_id:
        return f'#{el_id}'
    data_test = el.get_attribute("data-test")
    if data_test:
        return f"[data-test='{data_test}']"
    name = el.get_attribute("name")
    if name:
        return f"{tag} [name='{name}']"
    classes = [c for c in (el.get_attribute("class") or "").split() if c]
    if classes:
        return tag + "".join(f'.{c}' for c in classes[:3])
    role = el.get_attribute("role")
    if role:
        return f"{tag} [role='{role}']"
    typ = el.get_attribute("type")
    if typ:
        return f"{tag} [type='{typ}']"
    return tag


# # wypisanie kandydatów
# count = 0
# seen = set()
# for i, el in enumerate(candidates, 1):
#     text = (el.text or "").strip()
#     selector = css_for(el)
#     if selector in seen:
#         continue
#     seen.add(selector)
#     print(f"{i:02d}. {selector} | text='{text}'")



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, TimeoutException
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(headless=False, window_size=(1920, 1080)):
    chrome_options = Options()

    # tryb headless
    if headless:
        chrome_options.add_argument("--headless=new") # (chrome 109+)
        # chrome_options.add_argument("--headless")

    # rozmiar okna
    chrome_options.add_argument(f"window-size={window_size[0]},{window_size[1]}")
    chrome_options.add_argument("--window-position=0,0")

    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--start-fullscreen")

    chrome_options.add_argument("--kiosk")  # bez UI

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--disable-web-security")

    chrome_options.add_argument("--allow-running-insecure-content")  # pozwala na HTTP

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--disable-software-rasterizer")   # wyłączenie acceleration

    # procesy w tle
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-renderer-backgrounding")

    chrome_options.add_argument("--hide-scrollbars")

    chrome_options.add_argument("--disable-infobars")  # ukryj "chrome is controlled...."

    chrome_options.add_argument("--no-default-browser-check")

    # wyłączenie powiadomień
    chrome_options.add_argument("--disable-notifications")

    # logowanie
    chrome_options.add_argument("--log-level=3")  # 0=INFO, 1=WARNING, 2=LOG_ERROR, 3=LOG_FATAL
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--disable-logging")

    chrome_options.add_argument("--lang=pl")  # Język polski
    chrome_options.add_argument("--lang=en-US")  # Język angielski
    chrome_options.add_argument("--accept-lang=pl,en;q=0.9")

    driver = webdriver.Chrome(options=chrome_options)

    # Wykonaj skrypt JavaScript aby ukryć automatyzację
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver

# driver = setup_driver(False, (200, 300))


# Zarządzanie oknem przeglądarki
def browser_management(driver):
    driver.maximize_window()
    driver.set_window_size(1200, 800)
    driver.minimize_window()
    windows_size = driver.get_window_size()
    window_position = driver.get_window_position()

# cookies
def handle_cookies_and_storage(driver):
    driver.add_cookies({
        'name': 'test_cookies',
        'values': 'cookie_value'
    })
    cookies =driver.get_cookies()
    driver.delete_all_cookie()

def javascript_execution(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Do dołu
    sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")  # Do góry
    element = driver.execute_script("return document.querySelector('[data-test=\"username\"]');")

def handle_alerts(driver):
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

    except TimeoutException:
        print('Alert nie pojawił się')

def handle_windows_and_frames(driver):
    driver.execute_script("window.open('https://www.google.com', '_blank');")
    windows = driver.window_handles   # pobieranie listy wszystkich okien
    # Przełączenie na nowe okno
    if len(windows) > 1:
        driver.switch_to.window(windows[1])
        print(f"Tytuł nowego okna: {driver.title}")
    driver.close()
    driver.switch_to.window(windows[0])

    # przełączanie między ramkami:
    try:
        driver.switch_to.frame("nazwa")
        # driver.switch_to.frame(0)
        # driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        driver.switch_to.default_content()
    except NoSuchElementException:
        print("ramka nieznaleziona")