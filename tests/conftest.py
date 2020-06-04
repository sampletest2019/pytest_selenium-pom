import platform
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():

    if 'Win' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_83.exe")
    elif 'Mac' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_83.exe")

    # wait 10 seconds till the website will open
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # when test is done, close ALL windows of the browser
    browser.quit()