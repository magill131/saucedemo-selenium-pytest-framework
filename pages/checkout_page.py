from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def fill_info(self, first_name, last_name, postal_code):
        if first_name:
            self.type(self.FIRST_NAME, first_name)
        if last_name:
            self.type(self.LAST_NAME, last_name)
        if postal_code:
            self.type(self.POSTAL_CODE, postal_code)
        return self

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)

    def error_message(self):
        return self.text_of(self.ERROR)

    def overview_item_names(self):
        self.wait_for_url_contains("checkout-step-two")
        return [el.text for el in self.find_all(self.SUMMARY_ITEM_NAMES)]

    def finish(self):
        self.click(self.FINISH_BUTTON)

    def confirmation_text(self):
        self.wait_for_url_contains("checkout-complete")
        return self.text_of(self.COMPLETE_HEADER)
