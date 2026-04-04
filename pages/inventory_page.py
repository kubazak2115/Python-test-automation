from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class InventoryPage(BasePage):

    #locators

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".inventory_item button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    #

    def open(self):
        super().open("/inventory.html")

    def get_page_title(self) -> str:
        return self.find(self.PAGE_TITLE).text
    
    def get_product_count(self) -> int:
        # return len(self.find_all(self.PRODUCT_ITEMS))
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
    
    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        if buttons:
            buttons[0].click()
        
    def add_item_to_cart_by_index(self, index: int):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        # if 0 <= index < len(buttons):
        buttons[index].click()
    
    def get_cart_count(self) -> int:
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0
    
    def go_to_cart(self):
        self.find_clickable(self.CART_LINK).click()
    
    def get_product_names(self) -> list[str]:
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]
    
    def get_product_prices(self) -> list[float]:
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]
    
    def sort_by(self, option_value: str):
        """ option_value can be: 'az', 'za', 'lohi', 'hilo' """
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN)).select_by_value(option_value)
    
    def logout(self):
        self.find_clickable(self.BURGER_MENU).click()
        time.sleep(0.5)
        self.find_clickable(self.LOGOUT_LINK).click()

    def get_title(self) -> str:
        return self.find((By.CLASS_NAME, "title")).text