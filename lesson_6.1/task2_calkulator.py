from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from time import sleep

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait = driver.find_element(By.CSS_SELECTOR,"#delay")
wait.clear()

waiting_timer = 5
wait.send_keys(waiting_timer)

driver.find_element(By.XPATH,"//span[@class='btn btn-outline-primary' and text()='7']").click()
driver.find_element(By.XPATH,"//span[@class='operator btn btn-outline-success' and text()='+']").click()
driver.find_element(By.XPATH,"//span[@class='btn btn-outline-primary' and text()='8']").click()
driver.find_element(By.XPATH,"//span[@class='btn btn-outline-warning' and text()='=']").click()

sleep(waiting_timer)

result = driver.find_element(By.CSS_SELECTOR,".top .screen").text

@pytest.mark.parametrize("int",[(int(result))])
def test_calculator(int):
    assert int == 15

driver.quit()