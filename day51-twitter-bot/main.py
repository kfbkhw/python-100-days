from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWNS = 150
PROMISED_UPS = 10
EMAIL = "haileyprogramming@gmail.com"
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


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
