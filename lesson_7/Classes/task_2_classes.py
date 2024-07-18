from selenium.webdriver.common.by import By
from time import sleep


class Calculator:

    def __init__(self,driver):
        self._driver = driver
    
    def set_timer(self,sec):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait = self._driver.find_element(By.CSS_SELECTOR,"#delay")
        wait.clear()
        wait.send_keys(sec)

    def press_buttons_watit(self,sec):
        self._driver.find_element(By.XPATH,"//span[@class='btn btn-outline-primary' and text()='7']").click()
        self._driver.find_element(By.XPATH,"//span[@class='operator btn btn-outline-success' and text()='+']").click()
        self._driver.find_element(By.XPATH,"//span[@class='btn btn-outline-primary' and text()='8']").click()
        self._driver.find_element(By.XPATH,"//span[@class='btn btn-outline-warning' and text()='=']").click()

        sleep(sec)

        result = self._driver.find_element(By.CSS_SELECTOR,".top .screen").text
        
        return result