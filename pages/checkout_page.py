from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    # locators
    # setp 1
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    CHECKOUT_BTN = (By.ID, "checkout")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # step 2
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BTN = (By.ID, "finish")

    # step 3
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.find(self.FIRST_NAME).send_keys(first_name)
        self.find(self.LAST_NAME).send_keys(last_name)
        self.find(self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.find_clickable(self.CONTINUE_BTN).click()
    
    def get_error_message(self) -> str:
        return self.find(self.ERROR_MESSAGE).text
    
    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
    
    def get_item_total(self) -> float:
        text = self.find(self.ITEM_TOTAL).text
        return float(text.split("$")[1])
    
    def get_tax(self) -> float:
        text = self.find(self.TAX).text
        return float(text.split("$")[1])
    
    def get_total(self) -> float:
        text = self.find(self.TOTAL).text
        return float(text.split("$")[1])
    
    def click_finish(self):
        self.find_clickable(self.FINISH_BTN).click()
    
    def get_confirmation_message(self) -> str:
        return self.find(self.CONFIRM_HEADER).text
    
    def is_order_confirmed(self) -> bool:
        return self.is_visible(self.CONFIRM_HEADER)
    
    def go_back_home(self):
        self.find_clickable(self.BACK_HOME_BTN).click()

    def is_on_step_two(self) -> bool:
        return self.is_visible(self.FINISH_BTN)

    def is_on_inventory_page(self) -> bool:
        return "/inventory.html" in self.driver.current_url
