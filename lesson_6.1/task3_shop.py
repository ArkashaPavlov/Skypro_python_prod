from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR,"#login-button").click()

driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a").click()

driver.find_element(By.CSS_SELECTOR,"#checkout").click()

driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Palkovodets")
driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Bobrow")
driver.find_element(By.CSS_SELECTOR,"#postal-code").send_keys("9112281488")

driver.find_element(By.CSS_SELECTOR,"#continue").click()


total_prise = driver.find_element(By.XPATH,"//div[@class='summary_total_label']").text

driver.quit()

index = total_prise.find('$')
final_price = total_prise[index:]

@pytest.mark.parametrize("sum",[((final_price))])
def test_prise(sum):
    assert sum == "$58.29"
