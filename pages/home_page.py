"""
This module contains page object for All Videos page.
Limited functionality only.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AllVideosPage:

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = 'https://www.allvideos.com'
    PAGE_TITLE = 'All Videos'

    # Element Locators
    VIDEOS_TABLE = (By.ID, "videostable")
    TABLE_ROWS = VIDEOS_TABLE.find_elements(By.TAG_NAME, "tr")

    BLACK_FRAMES_ADJUST_BUTTON = (By.ID, "blackframeadjust")
    BLACK_FRAMES_REDUCE_BUTTON = (By.ID, "blackframereduce")
    ORIGINAL_CLIP_DURATION = (By.ID, "originalduration")

    # Methods
    def load_page(self):
        self.browser.get(self.URL)

    def assert_page_title(self):
        assert self.browser.title == self.PAGE_TITLE

    def click_specific_row(self, row):
        self.TABLE_ROWS[row].click()

    def get_video_time(self, row):
        all_cells = self.TABLE_ROWS[row].find_elements(By.TAG_NAME, "td")
        video_time = all_cells[0].text
        return video_time

    def assert_video_length(self, expected_length, row):
        all_cells = self.TABLE_ROWS[row].find_elements(By.TAG_NAME, "td")
        video_time = all_cells[0].text
        assert video_time == expected_length

    def get_video_duration(self, row):
        all_cells = self.TABLE_ROWS[row].find_elements(By.TAG_NAME, "td")
        video_duration = all_cells[1].text
        return video_duration

    def assert_video_duration(self, expected_duration, row):
        all_cells = self.TABLE_ROWS[row].find_elements(By.TAG_NAME, "td")
        video_duration = all_cells[1].text
        assert video_duration == expected_duration

    def adjust_clip_duration(self):
        self.browser.find_element(self.BLACK_FRAMES_ADJUST_BUTTON).click()

    def decrease_clip_duration(self):
        self.browser.find_element(self.BLACK_FRAMES_REDUCE_BUTTON).click()

