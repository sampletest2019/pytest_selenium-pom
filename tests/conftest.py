import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    browser = webdriver.Chrome("../resources/chromedriver_83.exe")
    # use this path if you are on Mac Os
    # browser = webdriver.Chrome("../resources/chromedriver_mac_83.exe")
    # wait 10 seconds till the website will open
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # when test is done, close ALL windows of the browser
    browser.quit()