from selenium import webdriver
import pytest

from Classes.task_2_classes import Calculator

driver = webdriver.Chrome()
sec = 1

calc = Calculator(driver)
calc.set_timer(sec)

@pytest.mark.parametrize("int",[(int(calc.press_buttons_watit(sec)))])
def test_calculator(int):
    assert int == 15

driver.quit()