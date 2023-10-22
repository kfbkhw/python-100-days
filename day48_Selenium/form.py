from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("John")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Doe")
email = driver.find_element(By.NAME, value="email")
email.send_keys("johndoe@email.com")
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()
