from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    # locators

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='remove']")
    CONTINUE_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_title(self) -> str:
        return self.find(self.PAGE_TITLE).text

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))
    
    def get_item_names(self) -> list:
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]
    
    def get_item_prices(self) -> list:
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]
    
    def remove_item_by_index(self, index: int):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if 0 <= index < len(buttons):
            buttons[index].click()
    
    def remove_all_items(self):
        while True:
            buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if not buttons:
                break
            buttons[0].click()    
            
    def continue_shopping(self):
        self.find_clickable(self.CONTINUE_BTN).click()
    
    def proceed_to_checkout(self):
        self.find_clickable(self.CHECKOUT_BTN).click()
    
    def is_empty(self) -> bool:
        return self.get_item_count() == 0