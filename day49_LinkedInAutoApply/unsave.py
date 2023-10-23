import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

EMAIL = "haileyprogramming@gmail.com"
PASSWORD = "hailey0#"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/my-items/saved-jobs/")

time.sleep(1)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(2)

try:
    while True:
        menu = driver.find_element(By.CSS_SELECTOR, "div.entity-result__actions-overflow-menu-dropdown > div:nth-child(1) > button")
        menu.click()
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "div.entity-result__actions-overflow-menu-dropdown > div:nth-child(1) > div > div > div:nth-child(4)")
        button.click()
        time.sleep(1)
except NoSuchElementException:
    pass
