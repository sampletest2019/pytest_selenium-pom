import platform
import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def browser():
    chrome_version_win = "89"
    chrome_version_mac = "89"
    chrome_version_linux = "89"

    if 'Win' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_win_{}.exe".format(chrome_version_win))
    elif 'darwin' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
    elif 'macOS' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
    elif 'linux' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_linux_{}".format(chrome_version_linux))
    else:
        raise Exception("chromedriver is not configured for your Operation System! "
                        "Your Operating System is: {}".format(platform.platform()))

    # wait 10 seconds to pull the DOM
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # make a screenshot before closing the browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # when test is done, close ALL windows of the browser
    browser.quit()