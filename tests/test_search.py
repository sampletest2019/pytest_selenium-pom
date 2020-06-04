from pytest_selenium_simple.pages.home_page import AmazonHomePage
from pytest_selenium_simple.pages.search_result_page import AmazonSearchResultPage

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
search_title = 'Amazon.com : nike air max'


def test_search_airmax(browser):
    home_page = AmazonHomePage(browser)
    search_result_page = AmazonSearchResultPage(browser)
    search_item = 'nike air max'

    # navigate to Amazon.com home page
    home_page.load_page()

    # verify that web page title is Amazon.com
    home_page.check_title()

    # search for Nike Air Max
    home_page.search_item(search_item)

    # verify that web page title contains Nike Air Max
    search_result_page.check_title()
