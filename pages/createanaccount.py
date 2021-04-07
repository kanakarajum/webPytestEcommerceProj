import time

from selenium.webdriver.common.by import By

from constants.constants import Constants
from pages.basepage import BasePage
from tests.baseClass import BaseClass


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
    COUNTRY_DRPDWN = (By.XPATH, "(//select[@id='id_country']//option)[2]")
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
    def fill_register_from(self, getDataForCreateAnAccountDist):
        BaseClass.appSync(self, Constants.SLEEP_TIME)
        assert self.is_displayed(CreateAnAccount.CREATE_AN_ACCOUNT_HEADER)
        assert self.get_element_text(
            CreateAnAccount.CREATE_AN_ACCOUNT_HEADER).upper() == Constants.CREATE_AN_ACCOUNT_HEADER.upper()
        # select the gender title
        if getDataForCreateAnAccountDist['title'] == "Mr":
            CreateAnAccount.get_gender_option(self, CreateAnAccount.MR_RADIOBUTTON).click()
        elif getDataForCreateAnAccountDist['title'] == "Mrs":
            CreateAnAccount.get_gender_option(self, CreateAnAccount.MRS_RADIOBUTTON).click()
        # Enter FirstName
        self.do_send_keys(CreateAnAccount.FIRSTNAME_TXTBX, getDataForCreateAnAccountDist['firstname'])
        # Enter LastName
        self.do_send_keys(CreateAnAccount.LASTNAME_TXTBX, getDataForCreateAnAccountDist['lastname'])
        # get the prefill email val and match with email enter at start
        strPrefillEmailVal = self.get_attribute_value(CreateAnAccount.EMAIL_TXTBX, "value").strip()
        assert strPrefillEmailVal != ""
        # Enter password
        self.do_send_keys(CreateAnAccount.PASSWORD_TXTBX, getDataForCreateAnAccountDist['password'])
        # select DAY/MONTH/YEAR from dropdown
        self.do_select_val_from_dropdown("value", CreateAnAccount.DATE_OF_BIRTH_DAYS_DRPDWN,
                                         getDataForCreateAnAccountDist['date'])
        self.do_select_val_from_dropdown("value", CreateAnAccount.DATE_OF_BIRTH_MONTHS_DRPDWN,
                                         getDataForCreateAnAccountDist['month'])
        self.do_select_val_from_dropdown("value", CreateAnAccount.DATE_OF_BIRTH_YEARS_DRPDWN,
                                         getDataForCreateAnAccountDist['year'])
        # SELECT AN CHECKBOX
        self.do_select_an_checkbox(CreateAnAccount.SIGNUP_FOR_NEWSLETTER_CHKBX)
        # PREFILL FIRST NAME AND LAST NAME VERIFICATION
        strprefilladdressfirstname = self.get_attribute_value(CreateAnAccount.ADDRESS_FIRSTNAME_TXTBX, "value").strip()
        assert strprefilladdressfirstname == getDataForCreateAnAccountDist['firstname']
        strprefilladdresslastname = self.get_attribute_value(CreateAnAccount.ADDRESS_LASTNAME_TXTBX, "value").strip()
        assert strprefilladdresslastname == getDataForCreateAnAccountDist['lastname']
        # Enter Address
        self.do_send_keys(CreateAnAccount.ADDRESS_TXTBX, getDataForCreateAnAccountDist['address'])
        # Enter City
        self.do_send_keys(CreateAnAccount.CITY_TXTBX, getDataForCreateAnAccountDist['city'])
        # Select state
        self.do_select_val_from_dropdown("visible text", CreateAnAccount.STATE_DRPDWN,
                                         getDataForCreateAnAccountDist['state'])
        # Enter ZipCode
        self.do_send_keys(CreateAnAccount.ZIPCODE_TXTBX, getDataForCreateAnAccountDist['zipcode'])
        # verify prefill Country
        assert self.get_attribute_value(CreateAnAccount.COUNTRY_DRPDWN,
                                        "text").strip() == Constants.COUNTRY_UNITED_STATES
        # Enter Mobile Phone
        self.do_send_keys(CreateAnAccount.MOBILEPHONE_TXTBX, getDataForCreateAnAccountDist['mobilephone'])
        # Address alias
        self.do_clear(CreateAnAccount.ADDRESSALIAS_TXTBX)
        self.do_send_keys(CreateAnAccount.ADDRESSALIAS_TXTBX, getDataForCreateAnAccountDist['addressAlias'])
        # Click on Register button
        self.do_click(CreateAnAccount.REGISTER_BTN)
