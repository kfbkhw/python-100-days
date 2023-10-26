import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

EMAIL = "haileyprogramming@gmail.com"
PASSWORD = "haileycoding"
count = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://tinder.com/")

time.sleep(2)
login = driver.find_elements(By.CSS_SELECTOR, "div.l17p5q9z")[1]
login.click()

time.sleep(2)
facebook_login = driver.find_elements(By.CSS_SELECTOR, "div.Typs\(button-1\)")[0]
facebook_login.click()

time.sleep(2)
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD+Keys.ENTER)

time.sleep(5)
driver.switch_to.window(tinder_window)

time.sleep(5)
decline_cookies = driver.find_element(By.CSS_SELECTOR, "div.D\(f\)--ml > div:nth-child(2) > button > div.w1u9t036 > div.l17p5q9z")
decline_cookies.click()

time.sleep(3)
allow_location = driver.find_elements(By.CSS_SELECTOR, "div.l17p5q9z")[0]
allow_location.click()

time.sleep(3)
decline_notification = driver.find_elements(By.CSS_SELECTOR, "div.l17p5q9z")[1]
decline_notification.click()

for n in range(20):
    try:
        time.sleep(2)
        dislike = driver.find_element(By.CSS_SELECTOR, "div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-nope-default\) > button")
        dislike.click()
        count += 1
    except NoSuchElementException:
        time.sleep(2)

print(f"Successfully disliked {count} people.")
