from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get('https://www.saucedemo.com/v1/')
driver.get('https://www.allegro.pl/')
sleep(20)

candidates = []
candidates += driver.find_elements(By.TAG_NAME, "button")
candidates += driver.find_elements(By.CSS_SELECTOR, "input[type='button'], input[type='submit']")
candidates += driver.find_elements(By.CSS_SELECTOR, "a[role='button'], [role='button']")

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

count = 1
for can in candidates:
    print(count, can)
    count += 1
    print(css_for(can))
    print()

# wypisanie kandydatów
count = 0
seen = set()
for i, el in enumerate(candidates, 1):
    text = (el.text or "").strip()
    selector = css_for(el)
    if selector in seen:
        continue
    seen.add(selector)
    print(f"{i:02d}. {selector} | text='{text}'")

driver.quit()