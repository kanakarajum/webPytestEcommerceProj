# THIS CLASS CONTAINS ALL THE TEST DATA
from constants.constants import Constants


class TestData:
    TESTDATA_REGISTER_AN_ACCOUNT = [
        {"title": "Mr", "firstname": "Jhon", "lastname": "Wick", "password": Constants.PASSWORD, "date": "10",
         "month": "1", "year": "1990", "address": "123 varick st", "city": "New york",
         "state": "New York", "zipcode": "10013", "country": "United States", "mobilephone": "7321011234",
         "addressAlias": "AddressNYC"}]

    TESTDATA_ITEMS_TO_SEARCH = [
        {"tshirt": "Faded Short Sleeve T-shirts", "blouse": "Blouse"}]

    TESTDATA_TO_SIGNIN = [{"emailID": "pytestauto+a01@gmail.com", "password": Constants.PASSWORD}]
