import random

from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.createanaccount import CreateAnAccount
from tests.baseClass import BaseClass


class AuthenticationPage(BasePage):
    # randomemailaddress = ""
    CREATE_AN_ACCOUNT_LBL = (By.XPATH, "//*[@id='create-account_form']//h3")
    ALREADY_REGISTERED_LBL = (By.XPATH, "//*[@id='login_form']//h3")
    CREATE_AN_ACCT_EMAIL_ADDRESS_TXTBX = (By.CSS_SELECTOR, "input#email_create")
    SIGN_IN_EMAIL_ADDRESS_TXTBX = (By.CSS_SELECTOR, "input#email")
    SIGN_IN_PASSWORD_TXTBX = (By.CSS_SELECTOR, "input#passwd")
    CREATE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button#SubmitCreate")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button#SubmitLogin")

    # '''CONSTRUCTOR - CALLING PARENT BasePage'''

    def __init__(self, driver):
        super().__init__(driver)

    # PAGE ACTIONS

    def get_create_an_account_header(self):
        actVal = self.get_element_text(AuthenticationPage.CREATE_AN_ACCOUNT_LBL)
        return actVal.upper()

    def is_createAnAcct_EmailAddressTxtBx_exists(self):
        return self.is_displayed(AuthenticationPage.CREATE_AN_ACCT_EMAIL_ADDRESS_TXTBX)

    def is_createAnAcct_button_exists(self):
        return self.is_displayed(AuthenticationPage.CREATE_AN_ACCOUNT_BUTTON)

    def sign_in_to_application(self, signInTestDataDict):
        assert self.is_displayed(AuthenticationPage.SIGN_IN_EMAIL_ADDRESS_TXTBX)
        self.do_clear(AuthenticationPage.SIGN_IN_EMAIL_ADDRESS_TXTBX)
        self.do_send_keys(AuthenticationPage.SIGN_IN_EMAIL_ADDRESS_TXTBX, signInTestDataDict['emailID'])
        assert self.is_displayed(AuthenticationPage.SIGN_IN_PASSWORD_TXTBX)
        self.do_send_keys(AuthenticationPage.SIGN_IN_PASSWORD_TXTBX, signInTestDataDict['password'])
        assert self.is_displayed(AuthenticationPage.SIGN_IN_BUTTON)
        self.do_click(AuthenticationPage.SIGN_IN_BUTTON)
        # return HomePage(self.driver)

    def create_an_new_account(self):
        # randomemailaddress = Constants.EMAIL_ADDRESS + str(random.randint(1, 100)) + "@gmail.com"
        randomemailaddress = BaseClass.generate_emailaddress(self)
        self.do_send_keys(AuthenticationPage.CREATE_AN_ACCT_EMAIL_ADDRESS_TXTBX,
                          randomemailaddress)
        self.do_click(AuthenticationPage.CREATE_AN_ACCOUNT_BUTTON)
        return CreateAnAccount(self.driver)
