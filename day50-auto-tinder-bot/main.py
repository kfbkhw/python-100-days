import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "haileyprogramming@gmail.com"
PASSWORD = "haileycoding"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://tinder.com/")

time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="s1166637769"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="s-561743307"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_login.click()

time.sleep(2)
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL+Keys.ENTER)
password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD+Keys.ENTER)

time.sleep(2)
driver.switch_to.window(tinder_window)
