import pytest

from src.pages.main import MainPage

@pytest.mark.smoke
@pytest.mark.skip
def test_page_title_not_none(driver):
    
    main_page = MainPage(driver)

    # given the website is displayed
    main_page.load()

    # then the website title is not none
    assert main_page.get_page_title() is not None
    