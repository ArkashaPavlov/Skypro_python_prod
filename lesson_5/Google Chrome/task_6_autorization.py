from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver_Chrome = webdriver.Chrome()

driver_Chrome.get("http://the-internet.herokuapp.com/login")

lok_login = driver_Chrome.find_element(By.CSS_SELECTOR, "#username")
lok_pass = driver_Chrome.find_element(By.CSS_SELECTOR, "#password")
lok_log_but = driver_Chrome.find_element(By.CSS_SELECTOR, "#login > button > i")

lok_login.send_keys("tomsmith")
lok_pass.send_keys("SuperSecretPassword")
sleep(2)

lok_log_but.click()