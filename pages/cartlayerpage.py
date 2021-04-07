from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class CartLayerPage(BasePage):
    PRODUCT_SUCCESSFULLY_ADDED_HEADER_TITLE = (
        By.XPATH, "//div[@id='layer_cart']//div[contains(@class,'layer_cart_product')]//h2")

    def __init__(self, driver):
        super().__init__(driver)

    # page actions
    def verify_product_successfully_added_to_cart_header(self):
        self.is_displayed(CartLayerPage.PRODUCT_SUCCESSFULLY_ADDED_HEADER_TITLE)
        return self.get_element_text(CartLayerPage.PRODUCT_SUCCESSFULLY_ADDED_HEADER_TITLE).strip()
