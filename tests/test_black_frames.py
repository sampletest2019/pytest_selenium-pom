import pytest
from pages.home_page import AllVideosPage


@pytest.mark.regressiontest
def test_black_frame_adjust(browser):
    home_page = AllVideosPage(browser)

    # navigate to All Videos home page
    home_page.load_page()
    # verify that web page title is All Videos
    home_page.assert_page_title()

    #Click on first row and save original time and duration of the first clip
    home_page.click_specific_row(0)
    clip_original_duration = home_page.get_video_duration(0)
    clip_original_time = home_page.get_video_time(0)

    #Adjust clip duration by clicking on + once
    home_page.adjust_clip_duration()

    #Assert clip time was increased on 5 sec and clip duration was increased on 5 sec
    home_page.assert_video_length(clip_original_time + 0.5, 0)
    home_page.assert_video_duration(clip_original_duration + 0.5, 0)


@pytest.mark.regressiontest
def test_black_frame_decrease(browser):
    home_page = AllVideosPage(browser)

    # navigate to All Videos home page
    home_page.load_page()
    # verify that web page title is All Videos
    home_page.assert_page_title()

    # Click on first row and save original time and duration of the first clip
    home_page.click_specific_row(0)
    clip_original_duration = home_page.get_video_duration(0)
    clip_original_time = home_page.get_video_time(0)

    # Decrease clip duration by clicking on - once
    home_page.decrease_clip_duration()

    # Assert clip time was decreased on 5 sec and clip duration was decreased on 5 sec
    home_page.assert_video_length(clip_original_time - 0.5, 0)
    home_page.assert_video_duration(clip_original_duration - 0.5, 0)
