# '''THIS PAGE CLASS CONTAINS ALL THE ELEMENT LOCATORS AND ITS PAGE ACTIONS'''
from selenium.webdriver.common.by import By

from pages.authenticationpage import AuthenticationPage
from pages.basepage import BasePage


class HomePage(BasePage):
    # '''BY LOCATORS/OR'''
    LOGO_HEADER = (By.XPATH, "//div[@id='header_logo']")
    SIGNIN_LINK = (By.CSS_SELECTOR, "a.login")
    SEARCH_QUERY_TXTBX = (By.XPATH, "//input[@id='search_query_top']")
    SEARCH_QUERY_BTN = (By.XPATH, "//button[contains(@class, 'button-search')]")

    # '''CONSTRUCTOR - CALLING PARENT BasePage'''

    def __init__(self, driver):
        super().__init__(driver)

    # '''PAGE ACTIONS'''

    def get_home_page_title(self, title):
        return self.get_page_title(title)

    def is_logo_header_exists(self):
        return self.is_displayed(self.LOGO_HEADER)

    def is_signin_link_exists(self):
        return self.is_displayed(self.SIGNIN_LINK)

    def is_searchQueryField_exists(self):
        return self.is_displayed(self.SEARCH_QUERY_TXTBX)

    def is_searchQueryButton_exists(self):
        return self.is_displayed(self.SEARCH_QUERY_BTN)

    def click_on_signin_link(self):
        self.do_click(self.SIGNIN_LINK)
        return AuthenticationPage(self.driver)