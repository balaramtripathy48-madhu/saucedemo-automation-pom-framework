from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Logout:
 def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    #locators
        self.menu = (By.ID,"react-burger-menu-btn")
        self.log_out = (By.LINK_TEXT,"Logout")

    #Actions

 def go_menu(self):
     self.wait.until(EC.element_to_be_clickable(self.menu)).click()

 def click_logout(self):
    self.wait.until(EC.element_to_be_clickable(self.log_out)).click()