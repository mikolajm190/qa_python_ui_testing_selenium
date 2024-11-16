'''
This module contains page object model for the form authentication page
of the https://the-internet.herokuapp.com/ website.
'''

from selenium.webdriver.common.by import By

from src.pages.abstract import AbstractPage
from src.pages.login.secure import SecureAreaPage

class FormLoginPage(AbstractPage):
    '''Class that models form auth page on https://the-internet.herokuapp.com/ website.'''

    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.TAG_NAME, 'button')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def input_username(self, username: str) -> None:
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def input_password(self, password: str) -> None:
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self) -> SecureAreaPage:
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return SecureAreaPage(self.driver)