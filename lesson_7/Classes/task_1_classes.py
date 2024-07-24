from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()

class Autorization:

    def init(self,driver):
        self._driver = driver

    def input_params(self,site="https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
        self._driver.get(site)
        self._driver.find_element(By.NAME,"first-name").send_keys(fake.name_male())
        self._driver.find_element(By.NAME,"last-name").send_keys(fake.last_name())
        self._driver.find_element(By.NAME,"address").send_keys(fake.address()) 
        self._driver.find_element(By.NAME,"city").send_keys(fake.city())
        self._driver.find_element(By.NAME,"country").send_keys(fake.country()) 
        self._driver.find_element(By.NAME,"e-mail").send_keys(fake.email()) 
        self._driver.find_element(By.NAME,"phone").send_keys(fake.phone_number()) 
        self._driver.find_element(By.NAME,"job-position").send_keys(fake.job()) 
        self._driver.find_element(By.NAME,"company").send_keys(fake.company()) 
        self._driver.find_element(By.TAG_NAME,"button").click()

    def check_status(self):
        stat_first_name = self._driver.find_element(By.ID,"first-name").get_attribute("class") 
        stat_last_name = self._driver.find_element(By.ID,"last-name").get_attribute("class") 
        stat_address = self._driver.find_element(By.ID,"address").get_attribute("class") 
        stat_city = self._driver.find_element(By.ID,"city").get_attribute("class") 
        stat_country = self._driver.find_element(By.ID,"country").get_attribute("class") 
        stat_e_mail = self._driver.find_element(By.ID,"e-mail").get_attribute("class") 
        stat_phone = self._driver.find_element(By.ID,"phone").get_attribute("class") 
        stat_job = self._driver.find_element(By.ID,"job-position").get_attribute("class") 
        stat_company = self._driver.find_element(By.ID,"company").get_attribute("class") 
        stat_zipC = self._driver.find_element(By.ID,"zip-code").get_attribute("class") 

        data_list = {
            "first_name" : stat_first_name,
            "last_name" : stat_last_name,
            "address" : stat_address,
            "city" : stat_city,
            "country" : stat_country,
            "e_mail" : stat_e_mail,
            "phone" : stat_phone,
            "job" : stat_job,
            "company" : stat_company,
            "zipC" : stat_zipC
        }
        
        return data_list