# THIS TEST CLASS HAS ALL TEST SCENARIOS FOR CREATE AN ACCOUNT FUNCTIONALITY
from constants.constants import Constants
from pages.homepage import HomePage
from testdata.testdata import TestData
from tests.baseClass import BaseClass


class Test_Authentication(BaseClass):

    def test_verifyCreateAnAccountUIElements(self):
        self.homepage = HomePage(self.driver)
        authenticationPage = self.homepage.click_on_signin_link()
        actHeaderVal = authenticationPage.get_create_an_account_header()
        assert actHeaderVal == Constants.CREATE_AN_ACCOUNT_HEADER.upper()
        assert authenticationPage.is_createAnAcct_EmailAddressTxtBx_exists()
        assert authenticationPage.is_createAnAcct_button_exists()
        self.account = authenticationPage.create_an_new_account()
