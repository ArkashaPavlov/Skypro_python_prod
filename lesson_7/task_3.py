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

f_name = generate_names(7)
l_name = generate_names(5)
phone = generate_nums(10)

first_page = Shop(driver)
first_page.autorization(login,password)
first_page.select_items()
first_page.chekout_form(f_name,l_name,phone) 

@pytest.mark.parametrize("sum",[((first_page.get_summ()))])
def test_prise(sum):
    assert sum == "$58.29"