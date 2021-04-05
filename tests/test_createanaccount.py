import pytest

from pages.homepage import HomePage
from testdata.testdata import TestData
from tests.baseClass import BaseClass


class Test_CreateAnAccount(BaseClass):

    def test_registerAnAccount(self, getDataForRegisterAnAccount):
        self.homepage = HomePage(self.driver)
        authenticationPage = self.homepage.click_on_signin_link()
        self.createanaccount = authenticationPage.create_an_new_account()
        self.createanaccount.create_an_new_account(getDataForRegisterAnAccount["title"])

    @pytest.fixture(params=TestData.TESTDATA_REGISTER_AN_ACCOUNT)
    def getDataForRegisterAnAccount(self, request):
        return request.param
