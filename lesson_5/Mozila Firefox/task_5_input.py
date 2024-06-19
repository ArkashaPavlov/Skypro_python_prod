from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver_Mozila = webdriver.Firefox()

driver_Mozila.get("https://the-internet.herokuapp.com/inputs")
sleep(3)

lok = driver_Mozila.find_element(By.CSS_SELECTOR, "#content > div > div > div > input[type=number]")

lok.send_keys("1000")
sleep(1)
lok.clear()
sleep(1)
lok.send_keys("999")
sleep(1)

driver_Mozila.quit()