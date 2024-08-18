from selenium.webdriver.common.by import By

class Shop:

    def __init__(self,driver):
        self._driver = driver
    
    def autorization(self,login,password):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,"#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR,"#login-button").click()

    def select_items(self):
        self._driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a").click()

    def chekout_form(self,f_nme,l_name,phone):
        self._driver.find_element(By.CSS_SELECTOR,"#checkout").click()
        self._driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys(f_nme)
        self._driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys(l_name)
        self._driver.find_element(By.CSS_SELECTOR,"#postal-code").send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR,"#continue").click()

    def get_summ(self):
        total_prise = self._driver.find_element(By.XPATH,"//div[@class='summary_total_label']").text
        self._driver.quit()
        index = total_prise.find('$')
        final_price = total_prise[index:]

        return final_price