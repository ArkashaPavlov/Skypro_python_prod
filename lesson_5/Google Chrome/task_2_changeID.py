from selenium import webdriver
from selenium.webdriver.common.by import By

driver_Chrome = webdriver.Chrome()

for i in range (3):
    driver_Chrome.get("http://uitestingplayground.com/dynamicid")
    lok = driver_Chrome.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    lok.click()