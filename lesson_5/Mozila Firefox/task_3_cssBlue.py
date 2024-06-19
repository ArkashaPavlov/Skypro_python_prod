from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.alert import Alert 


driver_Mozila = webdriver.Firefox()
driver_Mozila.get("http://uitestingplayground.com/classattr")

lok = driver_Mozila.find_element(By.XPATH,"//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]") 
lok.click()

sleep(1)
alert = Alert(driver_Mozila)

alert.accept()
sleep(1)

driver_Mozila.quit()