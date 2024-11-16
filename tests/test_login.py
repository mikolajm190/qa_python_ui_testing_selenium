import pytest
import os

from src.pages.main import MainPage

@pytest.mark.login
def test_form_auth_login(driver):
    
    main_page = MainPage(driver)

    # given the website is displayed
    main_page.load()

    # and user can click form authentication button
    form_auth_page = main_page.click_on_form_auth_link()

    # when user inputs valid username and password
    form_auth_page.input_username(os.environ["TEST_USERNAME"])
    form_auth_page.input_password(os.environ["TEST_PASSWORD"])

    # and clicks on login button
    secure_page = form_auth_page.click_login_button()

    # then the secure area pop up shows with message
    assert secure_page.get_banner_text().find('You logged into a secure area!') != -1
    