from selenium import webdriver

FOLLOW_ACCOUNT = "bestvacations"
USERNAME = "haileyprogramming"
PASSWORD = "haileycoding"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option("detach", True))

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
