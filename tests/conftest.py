import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from constants.constants import Constants

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")
    parser.addoption("--URL", action="store", default=Constants.AUT_URL)


@pytest.fixture(scope="class")
def setup(request):
    global driver
    print(">>>>>>>>>>>>>> I am in set up fixture >>>>>>>>>>>>>>>>>")
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()
    elif browser_name == "brave":
        browserOptions = webdriver.ChromeOptions()
        browserOptions.add_argument("--start-maximized")
        browserOptions.binary_location = Constants.BRAVE_APP_LOCATION
        objService = Service("{}{}".format(Constants.RESOURCES_DIR_PATH, "chromedriver"))
        driver = webdriver.Chrome(service=objService)
        # driver = webdriver.Chrome(executable_path=Constants.CHROME_EXECUTABLE_PATH, options=browserOptions)
    elif browser_name == "chrome":
        browserOptions = webdriver.ChromeOptions()
        # browserOptions.add_argument("start-fullscreen")
        # browserOptions.add_argument("--start-maximized")
        # browserOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        # browserOptions.add_experimental_option('useAutomationExtension', False)
        objService = Service("{}{}".format(Constants.RESOURCES_DIR_PATH, "chromedriver"))
        driver = webdriver.Chrome(service=objService)
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        objService = Service("{}{}".format(Constants.RESOURCES_DIR_PATH, "msedgedriver"))
        driver = webdriver.Edge(service=objService)
        driver.maximize_window()
    URL = request.config.getoption("--URL")
    driver.get(URL)
    request.cls.driver = driver
    yield
    print(">>>>>>>>>>>>>> I am in set up fixture - after YIELD >>>>>>>>>>>>>>>>>")
    driver.quit()
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    setup.get_screenshot_as_file(name)
