from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        if self.url:
            self.driver.get(self.url)
    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
    
    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))