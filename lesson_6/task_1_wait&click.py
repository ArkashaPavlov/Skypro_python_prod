from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

lok = driver.find_element(By.CSS_SELECTOR,"#ajaxButton")
lok.click()

waiter = WebDriverWait(driver,20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#content > p"), "Data loaded with AJAX get request.")
)

print(driver.find_element(By.CSS_SELECTOR,"#content > p").text)

driver.quit()