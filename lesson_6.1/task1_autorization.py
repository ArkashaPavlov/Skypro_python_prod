from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


driver = webdriver.Chrome()


def insert_click(site:str): 

    driver.get(site)

    driver.find_element(By.NAME,"first-name").send_keys("Иван")
    driver.find_element(By.NAME,"last-name").send_keys("Петров")
    driver.find_element(By.NAME,"address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME,"city").send_keys("Москва")
    driver.find_element(By.NAME,"country").send_keys("Россия")
    driver.find_element(By.NAME,"e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME,"phone").send_keys("+7985899998787")
    driver.find_element(By.NAME,"job-position").send_keys("QA")
    driver.find_element(By.NAME,"company").send_keys("SkyPro")
    driver.find_element(By.NAME,"zip-code")

    driver.find_element(By.TAG_NAME,"button").click()
    
    stat_first_name = driver.find_element(By.ID,"first-name").get_attribute("class")
    stat_last_name = driver.find_element(By.ID,"last-name").get_attribute("class")
    stat_address = driver.find_element(By.ID,"address").get_attribute("class")
    stat_city = driver.find_element(By.ID,"city").get_attribute("class")
    stat_country = driver.find_element(By.ID,"country").get_attribute("class")
    stat_e_mail = driver.find_element(By.ID,"e-mail").get_attribute("class")
    stat_phone = driver.find_element(By.ID,"phone").get_attribute("class")
    stat_job = driver.find_element(By.ID,"job-position").get_attribute("class")
    stat_company = driver.find_element(By.ID,"company").get_attribute("class")
    stat_zipC = driver.find_element(By.ID,"zip-code").get_attribute("class")

    result = [
        {"first_name" : stat_first_name},
        {"last_name" : stat_last_name},
        {"address" : stat_address},
        {"city" : stat_city},
        {"country" : stat_country},
        {"e_mail" : stat_e_mail},
        {"phone" : stat_phone},
        {"job" : stat_job},
        {"company" : stat_company},
        {"zipC" : stat_zipC}]

    return result


data_list =insert_click("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

data = {k: v for d in data_list for k, v in d.items()}


@pytest.mark.parametrize('text',[(data["zipC"])])
def test_ZIP(text):
    assert text == "alert py-2 alert-danger"


@pytest.mark.parametrize('text',[(data["first_name"]),(data["last_name"]),
    (data["address"]),(data["city"]),
    (data["country"]),(data["e_mail"]),
    (data["phone"]),(data["job"]),(data["company"])])
def test_rest(text):
    assert text == "alert py-2 alert-success"

driver.quit()