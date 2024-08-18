from selenium import webdriver 
import pytest 

from Classes.task_1_classes import Autorization

driver = webdriver.Chrome() 

auth = Autorization(driver)
auth.input_params()

@pytest.mark.parametrize('text',[(auth.check_status()["zipC"])]) 
def test_ZIP(text): #Проверяем что незаполненное поле zip-code - красное и с ошибкой
    assert text == "alert py-2 alert-danger" 

@pytest.mark.parametrize('text',[(auth.check_status()["first_name"]),(auth.check_status()["last_name"]),(auth.check_status()["address"]), #Задаются параметры для тестирования
                                 (auth.check_status()["city"]),(auth.check_status()["country"]),(auth.check_status()["e_mail"]),
                                 (auth.check_status()["phone"]),(auth.check_status()["job"]),(auth.check_status()["company"])]
                        )
def test_rest(text): #Проверяем что остальные поля зелёные и без ошибок
    assert text == "alert py-2 alert-success" 

driver.quit()