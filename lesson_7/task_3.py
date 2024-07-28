from selenium import webdriver
import random
import string

from Classes.task_3_classes import Shop

def generate_names(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
    
def generate_nums(char_num):
    return ''.join(random.choice(string.digits) for _ in range(char_num))

driver = webdriver.Chrome()

shop = Shop(driver)                     #Передаём драйвер в классы

def test_prise():
    login ="standard_user"
    password = "secret_sauce"
    f_name = generate_names(7)
    l_name = generate_names(5)
    phone = generate_nums(10)
    exp_summ = "$58.29"
    shop.autorization(login,password)       #авторизация
    shop.select_items()                     #Выброр товаров 
    shop.chekout_form(f_name,l_name,phone)  #Форма оформления заказа

    
    assert shop.get_summ() == exp_summ 