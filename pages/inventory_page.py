from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")

    def is_loaded(self):
        self.wait_for_url_contains("inventory.html")
        return self.text_of(self.TITLE) == "Products"

    def item_names(self):
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    def item_prices(self):
        return [float(el.text.replace("$", "")) for el in self.find_all(self.ITEM_PRICES)]

    def sort_by(self, visible_text):
        Select(self.find(self.SORT_DROPDOWN)).select_by_visible_text(visible_text)

    def add_item(self, index=0):
        self.find_all(self.ADD_BUTTONS)[index].click()

    def add_first_items(self, count):
        # Each click turns an "Add" button into "Remove", so the first Add button is always next.
        for _ in range(count):
            self.find_all(self.ADD_BUTTONS)[0].click()

    def remove_item(self, index=0):
        self.find_all(self.REMOVE_BUTTONS)[index].click()

    def cart_count(self):
        """Number on the cart badge, or 0 when the badge is not shown."""
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def open_cart(self):
        from pages.cart_page import CartPage

        self.click(self.CART_LINK)
        return CartPage(self.driver)

    def logout(self):
        from pages.login_page import LoginPage

        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
        return LoginPage(self.driver)

    def reset_app_state(self):
        self.click(self.MENU_BUTTON)
        self.click(self.RESET_LINK)
