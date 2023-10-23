import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

EMAIL = "haileyprogramming@gmail.com"
PASSWORD = "hailey0#"
saved = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3731561424&geoId=103588929&keywords=Python%20Developer&location=Seoul%2C%20South%20Korea&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

time.sleep(1)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
sign_in = driver.find_element(By.CSS_SELECTOR, 'div.login__form_action_container > button')
sign_in.click()


def save_jobs():
    global saved
    time.sleep(6)
    jobs = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container > li")
    for job in jobs[::20]:
        job.click()
        time.sleep(3)
        save = driver.find_element(By.CSS_SELECTOR, "div.job-details-jobs-unified-top-card__content--two-pane > div:nth-child(4) > div.display-flex > button")
        save.click()
        saved += 1
        time.sleep(2)
        dismiss_message = driver.find_element(By.CSS_SELECTOR, "div.artdeco-toasts_toasts > div:nth-child(1) > button")
        dismiss_message.click()
    print(f"{len(jobs)} jobs on this page.")


def move_to_next_page():
    time.sleep(2)
    current_page = driver.find_element(By.CSS_SELECTOR, "ul.artdeco-pagination__pages > li.selected")
    current_page_num = current_page.find_element(By.CSS_SELECTOR, "button > span").text
    print(f"Finished page {current_page_num}.\n")
    time.sleep(1)
    next_page = current_page.get_property("nextElementSibling")
    next_page.click()


try:
    while True:
        save_jobs()
        move_to_next_page()
except NoSuchElementException:
    pass

print(f"\n\nSaved {saved} job opportunities to your {EMAIL} LinkedIn account.")
