import pytest

from constants.constants import Constants
from pages.cartlayerpage import CartLayerPage
from pages.cartpage import CartPage
from pages.homepage import HomePage
from testdata.testdata import TestData
from tests.baseClass import BaseClass


class Test_SearchFunctionality(BaseClass):

    def test_SearchForProduct(self, getDataToSignIN, getDataToSearchProduct):
        homepage = HomePage(self.driver)
        cartpage = CartPage(self.driver)
        cartlayerpage = CartLayerPage(self.driver)
        authenticationpage = homepage.click_on_signin_link()
        authenticationpage.sign_in_to_application(getDataToSignIN)
        homepage.verify_search_functionality(getDataToSearchProduct['tshirt'])
        cartpage.click_add_to_cart_button()
        assert cartlayerpage.verify_product_successfully_added_to_cart_header() == Constants.PRODUCT_SUCCESSFULLY_ADDED_TO_CART_MESSAGE

    @pytest.fixture(params=TestData.TESTDATA_TO_SIGNIN)
    def getDataToSignIN(self, request):
        return request.param

    @pytest.fixture(params=TestData.TESTDATA_ITEMS_TO_SEARCH)
    def getDataToSearchProduct(self, request):
        return request.param
