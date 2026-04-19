import os
import sys
import glob
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# urls

BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://jsonplaceholder.typicode.com"

# credentials

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_USER = "locked_out_user"
PROBLEM_USER = "problem_user"

# driver fixture

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    browser = webdriver.Chrome(options=options)

    yield browser  

    browser.quit() 

# @pytest.fixture(scope="function")
# def logged_in_driver(driver):
    
#     from pages.login_page import LoginPage

#     login_page = LoginPage(driver, BASE_URL)
#     login_page.open()
#     login_page.login(VALID_USER, VALID_PASSWORD)
    
#     return driver

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    from pages.login_page import LoginPage
    from pages.cart_page import CartPage

    from pages.login_page import LoginPage

    login_page = LoginPage(driver, BASE_URL)
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)

    yield driver


