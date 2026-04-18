from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Checkout:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,100)

    #locators
    
        self.first_name = (By.NAME,"firstName")
        self.last_name = (By.ID,"last-name")
        self.postal_code = (By.NAME,"postalCode")
        self.go_continue = (By.NAME,"continue")
        self.final = (By.NAME,"finish")

    #Actions

    def enter_name(self,name):
        self.wait.until(EC.element_to_be_clickable(self.first_name)).send_keys(name)

    def enter_last_name(self,name_last):
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(name_last)

    def enter_zip_code(self,zip_code):
        self.wait.until(EC.element_to_be_clickable(self.postal_code)).send_keys(zip_code)
        
    def clic_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.go_continue)).click()

    def clic_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.final)).click()



        