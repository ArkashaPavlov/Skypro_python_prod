from selenium import webdriver
import pytest

from Classes.task_2_classes import Calculator

driver = webdriver.Chrome()
sec_to_wait = 45
Exp_result = 15

calc = Calculator(driver)
calc.set_timer(sec_to_wait)

@pytest.mark.parametrize("numb",[(int(calc.press_buttons_watit(sec_to_wait)))])
def test_calculator(numb):
    assert numb == Exp_result

driver.quit()