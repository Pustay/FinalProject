import requests
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

browser = testdata["browser"]
name = testdata['username']
passwd = testdata['password']


@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def err_401():
    return "401"


@pytest.fixture()
def hello_user():
    return "Hello, {}".format(name)


@pytest.fixture()
def find_header():
    return 'About Page'


@pytest.fixture()
def font_header():
    return '32px'

