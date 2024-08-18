from selenium import webdriver
from selenium.webdriver.common.by import By
from methoods import Employees
from selenium.webdriver.common.keys import Keys

import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

login = 'oleg@alltel24.ru'
password = '9xN$5qV*7qS&3sQ%'
pattern_name = "_ChildOfTests"
base_url = "https://lk.alltel24.ru/"

def get_auth_token(login, password):
    my_json = {
        "email": login,
         "password": password

    }

    response = requests.get(f"{base_url}api/auth/v1/auth/token-generate", json= my_json)
    resp_body = response.json()
    token = resp_body.get("data", {}).get("access_token")
    return token


@pytest.mark.parametrize('login, password',[(login, password)])
def test_login(login, password):
    driver = webdriver.Chrome()
    emps = Employees(driver)

    emps.log_in(login, password)
    start_page = driver.find_element(By.XPATH,"//h1[@class='animated fadeInDown']").text
    
    assert start_page == "Рабочий стол"
    driver.quit()


@pytest.mark.parametrize('login, password, pattern',[(login, password, pattern_name)])
def test_create(login, password, pattern):
    driver = webdriver.Chrome()
    emps = Employees(driver)
    wait = WebDriverWait(driver, 10)
    
    emps.log_in_emps(login, password)
    emps.create_user()
    driver.find_element(By.XPATH,"//button[contains(.,'Сохранить')]").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH,"/html/body/div[2]/div[3]")))

    emps.find_user(pattern)
    usesr_is_here = driver.find_element(By.XPATH,f"//p[contains(.,'{pattern}')]").is_displayed()

    assert usesr_is_here == True
    driver.quit()


@pytest.mark.parametrize('login, password, pattern',[(login, password, pattern_name)])
def test_create_internal(login, password, pattern):
    driver = webdriver.Chrome()
    emps = Employees(driver)

    emps.log_in_emps(login, password)
    emps.find_user(pattern)
    emps.add_internal()
    #Проверка глазами
    driver.quit()

@pytest.mark.parametrize('login, password, pattern',[(login, password, pattern_name)])
def test_change_user(login, password, pattern):
    driver = webdriver.Chrome()
    emps = Employees(driver)
    wait = WebDriverWait(driver, 10)
    
    emps.log_in_emps(login, password)
    emps.find_user(pattern)
    driver.find_element(By.XPATH,"//button[@title='Редактировать']").click()

    wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))

    driver.find_element(By.XPATH,"//input[@name='name']").click()
    driver.find_element(By.XPATH,"//input[@name='name']").send_keys(Keys.SHIFT + Keys.HOME)
    driver.find_element(By.XPATH,"//input[@name='name']").send_keys(Keys.DELETE)
    driver.find_element(By.XPATH,"//input[@name='name']").send_keys('changed_' + pattern)
    
    driver.find_element(By.XPATH,"//button[contains(.,'Сохранить')]").click()

    my_headers = {
        "Authorization": f"Bearer {get_auth_token(login, password)}",
        "Content-Type": "application/json"
        }

    my_params = {
        "limit": 20
        }
    response = requests.get(f"{base_url}api/company/v1/employee/list", params= my_params, headers= my_headers)
    resp_body = response.json()

    assert any(item["name"] == f'changed_{pattern}' for item in resp_body["data"]["list"])
    driver.quit()


@pytest.mark.parametrize('login, password, pattern',[(login, password, pattern_name)])
def test_change_internal(login, password, pattern):
    driver = webdriver.Chrome()
    emps = Employees(driver)
    wait = WebDriverWait(driver, 10)

    emps.log_in_emps(login, password)
    emps.find_user(pattern)
    driver.find_element(By.XPATH,"//button[@title='Редактировать']").click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Внутренние линии')]"))).click()
    driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[2]/div/div[3]/div/div/div[1]/div[1]").click() #Да, вот такой путь к элементу, по другому не вышло, это первый внутренний в списке 
    
    wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='userName']"))).click()
    username_field = driver.find_element(By.XPATH,"//input[@name='userName']")
    username_field.send_keys(Keys.SHIFT + Keys.HOME)
    username_field.send_keys(Keys.DELETE)
    username_field.send_keys("ti chego nadelal")
    driver.find_element(By.XPATH,"//button[@title='Сгенерировать']").click()
    
    save_botton = driver.find_element(By.XPATH,"//button[contains(.,'Сохранить')]")
    driver.execute_script("arguments[0].scrollIntoView();", save_botton)
    save_botton.click()
    
    #Проверка будет по АПИ. заправшиваем юзера, и вытягиваем номер внутреннего
    driver.quit()


@pytest.mark.parametrize('login, password',[(login, password)])
def test_check_statistic(login, password):
    driver = webdriver.Chrome()
    emps = Employees(driver)
    wait = WebDriverWait(driver, 10)
    
    emps.log_in(login, password)
    # wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='animated fadeInDown']")))

    driver.get("https://lk.alltel24.ru/statistics/standard/calls-form")

    wait.until(EC.presence_of_element_located((By.XPATH,"//button[@value='year']")))

    driver.find_element(By.XPATH,"//button[@value='year']").click()

    driver.find_element(By.XPATH,"//button[contains(.,'Поиск')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='css-th2l1r']")))
    search_result = driver.find_element(By.XPATH,"//button[contains(.,'Результаты поиска')]").text
    
    start_index = search_result.find("(") + 1
    end_index = search_result.find(")")
    count = search_result[start_index:end_index]

    assert count != "0"
    driver.quit()