from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random 
import string


class Employees:
    def random_char(self,char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    def __init__(self,driver):
       self._driver = driver

    def log_in(self,login,password):
        """
        Вход в ЛК
        """
        wait = WebDriverWait(self._driver, 10)

        self._driver.get("https://lk.alltel24.ru/sign-in")
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-email").click()
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-email").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR,"#signUp > button").click()
        wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='animated fadeInDown']")))


    def log_in_emps(self,login,password):
        """
        Вход в ЛК и переход на страницу сотрудников
        """
        wait = WebDriverWait(self._driver, 10)

        self._driver.get("https://lk.alltel24.ru/sign-in")
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-email").click()
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-email").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,"#usermodelweb-password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR,"#signUp > button").click()

        wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='animated fadeInDown']")))
        self._driver.get("https://lk.alltel24.ru/company/employee/list")

        wait.until(EC.presence_of_element_located((By.XPATH,"//button[@title='Редактировать']")))

    def create_user(self):
        """
        Создание одного юзера, без внутреннего. и без его сохранения.
        Паттерн имени - "_ChildOfTests" 
        """
        wait = WebDriverWait(self._driver, 10)

        User_name = self.random_char(5)+"_ChildOfTests"
        User_mail = self.random_char(7)+"@gmail.com"
           
        self._driver.find_element(By.CSS_SELECTOR,"#create-employee").click()
        self._driver.find_element(By.XPATH,"//input[@name='name']").click()
        self._driver.find_element(By.XPATH,"//input[@name='name']").send_keys(User_name)
        self._driver.find_element(By.XPATH,"//input[@name='email']").click()
        self._driver.find_element(By.XPATH,"//input[@name='email']").send_keys(User_mail)
        self._driver.find_element(By.XPATH,"//button[@title='Сгенерировать']").click()

    def find_user(self,name):
        """
        Поиск сотрудника по паттерну имени
        """
        self._driver.find_element(By.XPATH,"//*[@id='mui-1']").click()
        self._driver.find_element(By.XPATH,"//*[@id='mui-1']").clear()
        self._driver.find_element(By.XPATH,"//*[@id='mui-1']").send_keys(name)
        sleep(2)

    def add_internal(self):
        """
        Добавление внутреннего номера у уже существующего сотрудника
        """
        wait = WebDriverWait(self._driver, 10)

        self._driver.find_element(By.XPATH,"//button[@title='Редактировать']").click()
     
        wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(.,'Внутренние линии')]"))).click()

        self._driver.find_element(By.XPATH,"//button[contains(.,'Добавить линию')]").click()
        self._driver.find_element(By.XPATH,"//button[@title='Сгенерировать']").click()

        lok_line = self._driver.find_element(By.XPATH,"//div[label[contains(.,'Линия для исходящих звонков')]]") 
        lok_line.click()
        lok_line.find_element(By.TAG_NAME,"input").send_keys("мтт")
        lok_line.find_element(By.TAG_NAME,"input").send_keys(Keys.ENTER)

        self._driver.find_element(By.XPATH,"//button[contains(.,'Добавить')]").send_keys(Keys.ENTER)