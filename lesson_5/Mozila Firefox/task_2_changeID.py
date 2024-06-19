from selenium import webdriver
from selenium.webdriver.common.by import By

driver_Mozila = webdriver.Firefox()

for i in range (3):
    driver_Mozila.get("http://uitestingplayground.com/dynamicid")
    lok = driver_Mozila.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    lok.click()

driver_Mozila.quit()