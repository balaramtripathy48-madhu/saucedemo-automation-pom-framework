import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pages.saucedemo_login import LoginPage
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def logged_in(driver):
    login = LoginPage(driver)
    login.open_url()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.log_in()
    yield driver



