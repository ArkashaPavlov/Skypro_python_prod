from selenium import webdriver
import pytest

from Classes.task_3_classes import Shop

driver = webdriver.Chrome()

login ="standard_user"
password = "secret_sauce"

first_page = Shop(driver)
first_page.autorization(login,password)
first_page.select_items()
first_page.chekout_form("Palkovodets","Bobrow","9112281488") 


@pytest.mark.parametrize("sum",[((first_page.get_summ()))])
def test_prise(sum):
    assert sum == "$58.29"