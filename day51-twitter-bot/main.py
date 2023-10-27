from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWNS = 150
PROMISED_UPS = 10
EMAIL = "haileyprogramming@gmail.com"
USERNAME = "hailey149098737"
PASSWORD = "haileycoding"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option("detach", True))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        sleep(10)
        self.driver.execute_script("window.stop();")
        privacy_accept = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        privacy_accept.click()
        sleep(1)
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()
        sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")
        sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login.click()
        sleep(2)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(EMAIL+Keys.ENTER)
        sleep(2)
        try:
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(PASSWORD + Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.NAME, "text")
            username.send_keys(USERNAME+Keys.ENTER)
            sleep(2)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(PASSWORD + Keys.ENTER)
        sleep(4)
        try:
            close = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div')
            close.click()
            sleep(2)
        except NoSuchElementException:
            pass
        compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
        compose.click()
        sleep(2)
        message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/br')
        text = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWNS}down/{PROMISED_UPS}up?"
        message.send_keys(text)
        sleep(2)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div')
        post.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
