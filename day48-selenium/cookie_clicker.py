from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def cookie_clicker():
    cookie.click()
    current_time = time()
    return current_time


def item_checker():
    available_items = driver.find_elements(By.CSS_SELECTOR, "#store>div:not(.grayed")
    return available_items[-1]


game_start = time()
start = game_start
while True:
    end = cookie_clicker()
    if (end - start) >= 5:
        item_checker().click()
        start = time()
    elif (end - game_start) >= 300:
        break

cps = driver.find_element(By.ID, "cps")
print(cps.text)
