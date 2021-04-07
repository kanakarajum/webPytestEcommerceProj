from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class MyAccount(BasePage):
    MYACCOUNT_NAVELEMENT = (By.CSS_SELECTOR, "span.navigation_page")

    def __init__(self, driver):
        super().__init__(driver)

    def is_myaccount_navitem_displayed(self):
        assert self.is_displayed(MyAccount.MYACCOUNT_NAVELEMENT)
        print("Successfully register and in My Account page")
