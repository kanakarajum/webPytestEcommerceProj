# '''THIS BASEPAGE CLASS CONTAINS ALL THE COMMON ACTIONS METHODS'''
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator)).clear()

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

    # THIS METHOD RETURNS THE VALUE FROM AN GIVEN ATTRIBUTE
    def get_attribute_value(self, by_locator, attributetype):
        element = WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attributetype)

    def do_select_val_from_dropdown(self, method_of_select, by_locator, val):
        element = WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located(by_locator))
        objselect = Select(element)
        if method_of_select == "value":
            objselect.select_by_value(val)
        elif method_of_select == "index":
            objselect.select_by_index(val)
        elif method_of_select == "visible text":
            objselect.select_by_visible_text(val)

    def do_select_an_checkbox(self, by_locator):
        element = WebDriverWait(self.driver, Constants.TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located(by_locator)).click()

    def move_to_an_element(self, ele):
        # action = ActionChains(self.driver)
        # action.move_to_element(ele).perform()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
