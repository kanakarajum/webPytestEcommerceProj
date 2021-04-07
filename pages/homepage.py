# '''THIS PAGE CLASS CONTAINS ALL THE ELEMENT LOCATORS AND ITS PAGE ACTIONS'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from constants.constants import Constants
from pages.authenticationpage import AuthenticationPage
from pages.basepage import BasePage
from tests.baseClass import BaseClass


class HomePage(BasePage):
    # '''BY LOCATORS/OR'''
    LOGO_HEADER = (By.XPATH, "//div[@id='header_logo']")
    SIGNIN_LINK = (By.CSS_SELECTOR, "a.login")
    SEARCH_QUERY_TXTBX = (By.XPATH, "//input[@id='search_query_top']")
    SEARCH_QUERY_BTN = (By.XPATH, "//button[contains(@class, 'button-search')]")
    SEARCH_RESULT_HEADER = (By.XPATH, "//h1[contains(@class,'product-listing')]//span[@class='lighter']")
    SEARCH_PRODUCT_RESULTS = (By.XPATH, "//div[@class='product-container']")
    ADD_TO_CART_BTN = (By.XPATH, "//a[@title='Add to cart']")
    IN_STOCK_BTN = (By.XPATH, "//span[@class='availability']")

    # '''CONSTRUCTOR - CALLING PARENT BasePage'''

    def __init__(self, driver):
        super().__init__(driver)

    # dynamic page locators
    def get_ProductFromSearchResults(self, int_i):
        ProductFromSearchResults = (By.XPATH, "(//div[@class='product-container'])[" + str(int_i) + "]")
        return self.driver.find_element(*ProductFromSearchResults)

    def get_SearchResult_ProductNameTitle(self, int_i):
        SearchResult_ProductNameTitle = (
            By.XPATH, "(//div[@class='product-container'])[" + str(int_i) + "]//*[@class='product-name']")
        return self.driver.find_element(*SearchResult_ProductNameTitle)

    def get_SearchResult_ProductAddToCart(self, int_i):
        return self.driver.find_element(By.XPATH, "(//div[@class='product-container'])[" + str(
            int_i) + "]//div[@class='button-container']//a[@title='Add to cart']")

    def get_ProductSearchResults(self):
        return self.driver.find_elements(*HomePage.SEARCH_PRODUCT_RESULTS)

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

    def verify_search_functionality(self, itemtosearch):
        assert self.is_displayed(HomePage.SEARCH_QUERY_TXTBX)
        self.do_clear(HomePage.SEARCH_QUERY_TXTBX)
        self.do_send_keys(HomePage.SEARCH_QUERY_TXTBX, itemtosearch)
        self.do_click(HomePage.SEARCH_QUERY_BTN)
        BaseClass.appSync(self, Constants.SLEEP_TIME)
        actProductSerchResHeader = self.get_element_text(HomePage.SEARCH_RESULT_HEADER).strip()
        assert itemtosearch.upper() in actProductSerchResHeader.upper()
        ProductResults = HomePage.get_ProductSearchResults(self)
        i = 0
        for Product in ProductResults:
            i = i + 1
            if itemtosearch in Product.text.strip():
                Product.click()

    def click_on_signin_link(self):
        self.do_click(HomePage.SIGNIN_LINK)
        return AuthenticationPage(self.driver)
