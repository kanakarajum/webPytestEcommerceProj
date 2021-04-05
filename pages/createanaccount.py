import time

from selenium.webdriver.common.by import By

from constants.constants import Constants
from pages.basepage import BasePage


class CreateAnAccount(BasePage):
    CREATE_AN_ACCOUNT_HEADER = (By.XPATH, "//div[@id='noSlide']//h1")
    MR_RADIOBUTTON = "//input[@id='id_gender1']"
    MRS_RADIOBUTTON = "//input[@id='id_gender2']"
    FIRSTNAME_TXTBX = (By.CSS_SELECTOR, "input#customer_firstname")
    LASTNAME_TXTBX = (By.CSS_SELECTOR, "input#customer_lastname")
    EMAIL_TXTBX = (By.CSS_SELECTOR, "input#email")
    PASSWORD_TXTBX = (By.CSS_SELECTOR, "input#passwd")
    DATE_OF_BIRTH_DAYS_DRPDWN = (By.CSS_SELECTOR, "select#days")
    DATE_OF_BIRTH_MONTHS_DRPDWN = (By.CSS_SELECTOR, "select#months")
    DATE_OF_BIRTH_YEARS_DRPDWN = (By.CSS_SELECTOR, "select#years")
    SIGNUP_FOR_NEWSLETTER_CHKBX = (By.CSS_SELECTOR, "input#newsletter")
    ADDRESS_FIRSTNAME_TXTBX = (By.CSS_SELECTOR, "input#firstname")
    ADDRESS_LASTNAME_TXTBX = (By.CSS_SELECTOR, "input#lastname")
    ADDRESS_TXTBX = (By.CSS_SELECTOR, "input#address1")
    CITY_TXTBX = (By.CSS_SELECTOR, "input#city")
    STATE_DRPDWN = (By.CSS_SELECTOR, "select#id_state")
    ZIPCODE_TXTBX = (By.CSS_SELECTOR, "input#postcode")
    COUNTRY_DRPDWN = (By.CSS_SELECTOR, "select#id_country")
    MOBILEPHONE_TXTBX = (By.CSS_SELECTOR, "input#phone_mobile")
    ADDRESSALIAS_TXTBX = (By.XPATH, "//*[@id='address_alias']//input[@id='alias']")
    REGISTER_BTN = (By.CSS_SELECTOR, "button#submitAccount")

    GENDER_RADIOGRP = (By.XPATH, "//div[@class='radio-inline']//label")

    # '''CONSTRUCTOR - CALLING PARENT BasePage'''

    def __init__(self, driver):
        super().__init__(driver)

    # # DYNAMIC LOCATORS
    def get_gender_option(self, ele):
        objGender = (By.XPATH, ele)
        return self.driver.find_element(*objGender)

    # PAGE ACTIONS

    # THIS WILL CREATE AN NEW ACCOUNT
    def create_an_new_account(self, title_Mr_Mrs):
        time.sleep(5)
        assert self.is_displayed(CreateAnAccount.CREATE_AN_ACCOUNT_HEADER)
        assert self.get_element_text(
            CreateAnAccount.CREATE_AN_ACCOUNT_HEADER).upper() == Constants.CREATE_AN_ACCOUNT_HEADER.upper()
        if title_Mr_Mrs == "Mr":
            CreateAnAccount.get_gender_option(self, CreateAnAccount.MR_RADIOBUTTON).click()
        elif title_Mr_Mrs == "Mrs":
            CreateAnAccount.get_gender_option(self, CreateAnAccount.MRS_RADIOBUTTON).click()
