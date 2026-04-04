from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        super().open("/")

    def enter_username(self, username: str):
        field = self.find(self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)
    
    def enter_password(self, password: str):
        field = self.find(self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
    
    def click_login(self):
        self.find(self.LOGIN_BUTTON).click()
    
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    

    def get_error_message(self) -> str:
        return self.find(self.ERROR_MESSAGE).text
    
    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
    
    def is_on_inventory_page(self) -> bool:
        return "inventory" in self.driver.current_url

