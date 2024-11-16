import pytest
from src.pages.main import MainPage

@pytest.mark.loading
def test_loading(driver):

    EXPECTED_ELEMENT_TEXT = 'Hello World!'
    
    main_page = MainPage(driver)

    # given the website is displayed
    main_page.load()

    # and user can click loading and hidden loading links
    loading_page = main_page.click_on_loading_link().click_on_dynamic_loading_link()

    # when user selects option from dropdown
    loading_page.click_on_start_button()

    # then the option is selected
    assert loading_page.get_loading_element_text() == EXPECTED_ELEMENT_TEXT
    