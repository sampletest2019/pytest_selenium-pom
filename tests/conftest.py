import platform
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():

    chrome_version_win = '84'
    chrome_version_mac = '84'
    chrome_version_linux = '84'

    if 'Win' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_win_{{chrome_version_win}}.exe")
    elif 'Darwin' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_{{chrome_version_mac}}")
    elif "Linux" in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_linux_{{chrome_version_linux}}")
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