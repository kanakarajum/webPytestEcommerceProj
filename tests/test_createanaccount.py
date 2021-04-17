import pytest

from pages.homepage import HomePage
from pages.myaccount import MyAccount
from testdata.testdata import TestData
from tests.baseClass import BaseClass


class Test_CreateAnAccount(BaseClass):

    @pytest.mark.regression
    def test_registerAnAccount(self, getDataForCreateAnAccount):
        self.homepage = HomePage(self.driver)
        self.myaccount = MyAccount(self.driver)
        authenticationPage = self.homepage.click_on_signin_link()
        self.createanaccount = authenticationPage.create_an_new_account()
        self.createanaccount.fill_register_from(getDataForCreateAnAccount)
        self.myaccount.is_myaccount_navitem_displayed()

    @pytest.fixture(params=TestData.TESTDATA_REGISTER_AN_ACCOUNT)
    def getDataForCreateAnAccount(self, request):
        return request.param
