import pytest
from src.pages.main import MainPage

@pytest.mark.slider
def test_slider(driver):

    TEST_SLIDER_MOVES = 5
    EXPECTED_SLIDER_VALUE = '2.5'
    
    main_page = MainPage(driver)

    # given the website is displayed
    main_page.load()

    # and user can click dropdown link
    slider_page = main_page.click_on_slider_link()

    # when user selects option from dropdown
    slider_page.move_slider_n_times_right(TEST_SLIDER_MOVES)

    # then the option is selected
    assert slider_page.get_slider_value() == EXPECTED_SLIDER_VALUE
    