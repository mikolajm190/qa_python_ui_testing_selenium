'''
This module contains page object model for the main page
of the https://the-internet.herokuapp.com/ website.
'''

import os

from selenium.webdriver.common.by import By

from src.pages.abstract import AbstractPage
from src.pages.login.form_login import FormLoginPage
from src.pages.dropdown import DropdownPage
from src.pages.slider import SliderPage
from src.pages.loading.loading import LoadingPage

class MainPage(AbstractPage):
    '''Class that models main page on https://the-internet.herokuapp.com/ website.'''

    URL = os.environ["APP_URL"]

    FORM_AUTH_LINK = (By.LINK_TEXT, "Form Authentication")
    DROPDOWN_LINK = (By.LINK_TEXT, "Dropdown")
    SLIDER_LINK = (By.LINK_TEXT, "Horizontal Slider")
    LOADING_LINK = (By.LINK_TEXT, "Dynamic Loading")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def load(self) -> None:
        self.driver.get(self.URL)

    def get_page_title(self) -> str:
        return self.driver.title

    def click_on_form_auth_link(self) -> FormLoginPage:
        self.driver.find_element(*self.FORM_AUTH_LINK).click()
        return FormLoginPage(self.driver)
    
    def click_on_dropdown_link(self) -> DropdownPage:
        self.driver.find_element(*self.DROPDOWN_LINK).click()
        return DropdownPage(self.driver)
    
    def click_on_slider_link(self) -> SliderPage:
        self.driver.find_element(*self.SLIDER_LINK).click()
        return SliderPage(self.driver)
    
    def click_on_loading_link(self) -> LoadingPage:
        self.driver.find_element(*self.LOADING_LINK).click()
        return LoadingPage(self.driver)
