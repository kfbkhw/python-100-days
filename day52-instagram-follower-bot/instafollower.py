from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

FOLLOW_ACCOUNT = "bestvacations"
USERNAME = "haileyprogramming"
PASSWORD = "haileycoding"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option("detach", True))
        self.pop_up = None

    def login(self):
        sleep(2)
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(3)
        username = self.driver.find_elements(By.CSS_SELECTOR, "input._ac4d")[0]
        username.send_keys(USERNAME)
        sleep(1)
        password = self.driver.find_elements(By.CSS_SELECTOR, "input._ac4d")[1]
        password.send_keys(PASSWORD+Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(url=f"https://www.instagram.com/{FOLLOW_ACCOUNT}/")
        sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, "div._aa_y._aa_z._aa_- > header > section > ul > li:nth-child(2) > a")
        followers.click()
        sleep(3)
        self.pop_up = self.driver.find_element(By.CSS_SELECTOR, "div._aano")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.pop_up)

    def follow(self):
        sleep(2)
        self.driver.execute_script("arguments[0].scrollTop = 0", self.pop_up)
        sleep(2)
        follow_buttons = self.pop_up.find_elements(By.CSS_SELECTOR, "button._acan._acap._acat._aj1-")
        for button in follow_buttons:
            try:
                sleep(2)
                button.click()
            except ElementClickInterceptedException:
                close = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._a9_1")
                close.click()
                sleep(2)
                button.click()

