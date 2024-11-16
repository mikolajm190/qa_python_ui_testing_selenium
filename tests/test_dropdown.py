import pytest
from src.pages.main import MainPage

@pytest.mark.dropdown
def test_dropdown(driver):

    TEST_OPTION = "Option 1"
    
    main_page = MainPage(driver)

    # given the website is displayed
    main_page.load()

    # and user can click dropdown link
    dropdown_page = main_page.click_on_dropdown_link()

    # when user selects option from dropdown
    dropdown_page.select_dropdown_option(TEST_OPTION)

    # then the option is selected
    assert dropdown_page.get_active_dropdown_option() == TEST_OPTION
    