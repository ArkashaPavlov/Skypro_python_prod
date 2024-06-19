from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#----Chrome
driver_Chrome = webdriver.Chrome()

driver_Chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

serarch_loc = "#content > div > button"
lok = driver_Chrome.find_element(By.CSS_SELECTOR, serarch_loc)
need_to_press=0

for i in range (5):
    lok.send_keys(Keys.ENTER)
    need_to_press = need_to_press +1

print ("Chrome pressed bottom count = ", need_to_press)