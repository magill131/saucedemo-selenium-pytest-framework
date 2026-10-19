from selenium.webdriver.common.by import By

import config
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(config.BASE_URL)
        return self

    def enter_credentials(self, username, password):
        if username:
            self.type(self.USERNAME, username)
        if password:
            self.type(self.PASSWORD, password)
        return self

    def submit(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Log in and return the inventory page (use for valid logins)."""
        from pages.inventory_page import InventoryPage

        self.enter_credentials(username, password)
        self.submit()
        return InventoryPage(self.driver)

    def login_expecting_error(self, username, password):
        """Attempt a login that should fail and return the error message."""
        self.enter_credentials(username, password)
        self.submit()
        return self.text_of(self.ERROR)
