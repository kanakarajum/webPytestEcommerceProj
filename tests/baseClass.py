import random
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants

randomemailaddress = ""


@pytest.mark.usefixtures("setup")
class BaseClass:
    # global randomemailaddress

    def verifyPresenceOfElementWithLnkTxt(self, eleTxt):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, eleTxt)))

    def appSync(self, TIME_TO_WAIT):
        time.sleep(TIME_TO_WAIT)

    def generate_emailaddress(self):
        global randomemailaddress
        randomemailaddress = Constants.EMAIL_ADDRESS + str(random.randint(1, 100)) + "@gmail.com"
        return randomemailaddress
