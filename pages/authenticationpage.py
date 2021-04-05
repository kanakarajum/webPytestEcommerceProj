from selenium.webdriver.common.by import By

from constants.constants import Constants
from pages.basepage import BasePage
from pages.createanaccount import CreateAnAccount


class AuthenticationPage(BasePage):
    CREATE_AN_ACCOUNT_LBL = (By.XPATH, "//*[@id='create-account_form']//h3")
    ALREADY_REGISTERED_LBL = (By.XPATH, "//*[@id='login_form']//h3")
    CREATE_AN_ACCT_EMAIL_ADDRESS_TXTBX = (By.CSS_SELECTOR, "INPUT#email_create")
    SIGN_IN_EMAIL_ADDRESS_TXTBX = (By.CSS_SELECTOR, "INPUT#email")
    SIGN_IN_PASSWORD_TXTBX = (By.CSS_SELECTOR, "INPUT#passwd")
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

    def create_an_new_account(self):
        self.do_send_keys(AuthenticationPage.CREATE_AN_ACCT_EMAIL_ADDRESS_TXTBX, Constants.EMAIL_ADDRESS)
        self.do_click(AuthenticationPage.CREATE_AN_ACCOUNT_BUTTON)
        return CreateAnAccount(self.driver)