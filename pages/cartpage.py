from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.is_displayed(CartPage.ADD_TO_CART_BUTTON)
        self.do_click(CartPage.ADD_TO_CART_BUTTON)
