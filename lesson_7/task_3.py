from selenium import webdriver
import random
import string
import pytest

from Classes.task_3_classes import Shop

def generate_names(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
    
def generate_nums(char_num):
    return ''.join(random.choice(string.digits) for _ in range(char_num))

driver = webdriver.Chrome()

login ="standard_user"
password = "secret_sauce"
Exp_summ = "$58.29"

f_name = generate_names(7)
l_name = generate_names(5)
phone = generate_nums(10)

shop = Shop(driver)
shop.autorization(login,password)
shop.select_items()
shop.chekout_form(f_name,l_name,phone) 


@pytest.mark.parametrize("actual_sum",[((shop.get_summ()))])
def test_prise(actual_sum):
    assert actual_sum == Exp_summ