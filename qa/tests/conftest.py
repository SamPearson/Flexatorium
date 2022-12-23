import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from . import config
import re


# Adapt this file from the other project
# Then build out login_test
# Get the test suite running

def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://127.0.0.1:5000/",
                     help="Base URL for the application under test")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")

    driver_ = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver_.base_url = config.baseurl
    driver_.base_domain = re.sub(".*//","",config.baseurl)

    def quit_browser():
        driver_.quit()

    request.addfinalizer(quit_browser)
    return driver_

