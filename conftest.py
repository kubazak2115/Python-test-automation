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
    import os
    import glob

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    def get_chromedriver_path():
        wdm_base = os.path.expanduser(r"~\.wdm\drivers\chromedriver\win64")
        matches = glob.glob(os.path.join(wdm_base, "**", "chromedriver.exe"), recursive=True)
        if matches:
            return matches[0]
        raise FileNotFoundError("Nie znaleziono chromedriver.exe w ~/.wdm")

    service = Service(executable_path=get_chromedriver_path())
    browser = webdriver.Chrome(service=service, options=options) 
    browser.implicitly_wait(5)

    yield browser  

    browser.quit() 

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    
    from pages.login_page import LoginPage

    login_page = LoginPage(driver, BASE_URL)
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    return driver


