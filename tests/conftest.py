import platform
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():

    if 'Win' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_83.exe")
    elif 'Mac' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_83.exe")
    elif "Linux" in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_linux_83")
    else:
        raise Exception("chromedriver is not configured for your Operation System! "
                        "Your Operating System is: {}".format(platform.platform()))

    # wait 10 seconds to pull the DOM
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # when test is done, close ALL windows of the browser
    browser.quit()