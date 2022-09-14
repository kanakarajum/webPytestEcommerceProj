# '''THIS CLASS HAS ALL THE CONSTANTS'''
from pathlib import Path


class Constants:

    # GENERATE RESOURCE DIR PATH
    ROOT_DIR = Path(__file__).parent.parent
    RESOURCES_DIR_PATH = "{}{}".format(ROOT_DIR, "/resources/")

    # APPLICATION URL
    AUT_URL = "http://automationpractice.com/index.php"

    # DRIVERS PATH
    BRAVE_APP_LOCATION = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    LOG_FILE_PATH = "/Users/kanak/Documents/myAutomationSpace/pythonProjects/webPytestEcommerceProj/webPytestEcommerceProj/logs/logfile.log"

    # TIMEOUTS
    TIMEOUT_IN_SECONDS = 10
    SLEEP_TIME = 5

    # HOME PAGE CONSTANTS
    HOME_PAGE_TITLE = "My Store"

    # AUTHENTICATION PAGE CONSTANTS
    CREATE_AN_ACCOUNT_HEADER = "Create an account"
    ALREADY_REGISTERED_HEADER = "Already registered?"
    EMAIL_ADDRESS = "pytestauto"
    PASSWORD = "Pytest@123"
    COUNTRY_UNITED_STATES = "United States"

    FADED_SHORT_T_SHIRT = "Faded Short Sleeve T-shirts"
    PRODUCT_SUCCESSFULLY_ADDED_TO_CART_MESSAGE = "Product successfully added to your shopping cart"
