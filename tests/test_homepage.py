# '''THIS HAS ALL THE HOME PAGE TESTS'''
from constants.constants import Constants
from pages.homepage import HomePage
from tests.baseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_VerifyUserIsOnHomePage(self):
        homepage = HomePage(self.driver)
        actVal = homepage.get_home_page_title(Constants.HOME_PAGE_TITLE)
        assert actVal == Constants.HOME_PAGE_TITLE
        assert homepage.is_logo_header_exists()

    def test_VerifySearchQuerySection(self):
        homepage = HomePage(self.driver)
        assert homepage.is_searchQueryField_exists()
        assert homepage.is_searchQueryButton_exists()

    def test_VerifySignInLink(self):
        homepage = HomePage(self.driver)
        assert homepage.is_signin_link_exists()
