# '''THIS BASEPAGE CLASS CONTAINS ALL THE COMMON ACTIONS METHODS'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title):
        WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(EC.title_is(title))
        return self.driver.title

    def do_click(self, by_locator):
        WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locators, val):
        WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locators)).send_keys(val)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator))
        return element.text

    def do_select_an_radiobutton(self, by_locator):
        WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator)).click()
