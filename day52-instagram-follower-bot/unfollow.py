from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from instafollower import InstaFollower

bot = InstaFollower()
bot.login()

sleep(5)
profile = bot.driver.find_element(By.CSS_SELECTOR, "div.x1iyjqo2.xh8yej3 > div:nth-child(8) > div > span > div")
profile.click()


def find_followers():
    sleep(2)
    following = bot.driver.find_element(By.CSS_SELECTOR, "ul.x78zum5.x1q0g3np.xieb3on > li:nth-child(3)")
    following.click()
    sleep(2)
    pop_up = bot.driver.find_element(By.CSS_SELECTOR, "div._aano")
    for i in range(10):
        bot.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
    sleep(2)
    bot.driver.execute_script("arguments[0].scrollTop = 0", pop_up)


find_followers()

sleep(2)
following_buttons = bot.driver.find_elements(By.CSS_SELECTOR, "button._acan._acap._acat._aj1-")


def unfollow_followers():
    sleep(2)
    button.click()
    sleep(2)
    unfollow = bot.driver.find_element(By.CSS_SELECTOR, "button._a9--._a9-_")
    unfollow.click()


for button in following_buttons:
    try:
        unfollow_followers()
    except ElementClickInterceptedException:
        pass
