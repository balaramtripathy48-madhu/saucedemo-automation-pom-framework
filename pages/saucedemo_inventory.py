from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    #locators
        self.one_item = (By.NAME,"add-to-cart-sauce-labs-backpack")
        self.two_item = (By.NAME,"add-to-cart-sauce-labs-bike-light")
        self.third_item = (By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt")
        self.go_cart = (By.ID,"shopping_cart_container")
        
    #Actions

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.one_item)).click()
        self.wait.until(EC.element_to_be_clickable(self.two_item)).click()
        self.wait.until(EC.element_to_be_clickable(self.third_item)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.go_cart)).click()


    

