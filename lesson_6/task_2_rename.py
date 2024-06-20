from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput?")

lok_in = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

lok_in.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(text)