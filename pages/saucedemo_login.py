from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
     #locators
        self.username_input = (By.ID,"user-name")
        self.password_input = (By.ID,"password")
        self.login_btn = (By.ID,"login-button")
        
    #Actions

    def open_url(self):
        self.driver.get("https://saucedemo.com/")
    
    def enter_username(self,username):
        self.wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(username)

    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def log_in(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()