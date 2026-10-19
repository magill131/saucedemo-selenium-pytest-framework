from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "[data-test='continue-shopping']")

    def is_loaded(self):
        self.wait_for_url_contains("cart.html")
        return self.text_of(self.TITLE) == "Your Cart"

    def item_names(self):
        if not self.is_present(self.CART_ITEMS):
            return []
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove_item(self, index=0):
        self.find_all(self.REMOVE_BUTTONS)[index].click()

    def continue_shopping(self):
        from pages.inventory_page import InventoryPage

        self.click(self.CONTINUE_SHOPPING)
        return InventoryPage(self.driver)

    def checkout(self):
        from pages.checkout_page import CheckoutPage

        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)
