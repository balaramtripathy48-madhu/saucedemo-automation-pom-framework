from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)
    #locators
        self.remove_item = (By.ID,"remove-sauce-labs-backpack")
        self.continue_shopping = (By.ID,"continue-shopping")
        self.any_item = (By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        self.check_out = (By.ID,"checkout")

    #Actions

    def remove_any_item(self):
          self.wait.until(EC.element_to_be_clickable(self.remove_item)).click()

    def scroll_down(self):
          self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        
    def back_to_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_shopping)).click()

    def add_any_item(self):
         self.wait.until(EC.element_to_be_clickable(self.any_item)).click()

    def scroll_top(self):
         self.driver.execute_script("window.scrollTo(0, 0);")

    def go_to_checkout(self):
         self.wait.until(EC.element_to_be_clickable(self.check_out)).click()

         
         
         
          
         