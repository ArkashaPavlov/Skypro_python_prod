from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver_Chrome = webdriver.Chrome()

driver_Chrome.get("https://the-internet.herokuapp.com/entry_ad")
lok = driver_Chrome.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")

sleep(1)

lok.click()