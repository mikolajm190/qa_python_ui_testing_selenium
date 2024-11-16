from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from src.pages.abstract import AbstractPage

class SliderPage(AbstractPage):

    SLIDER = (By.TAG_NAME, 'input')
    SLIDER_VALUE = (By.ID, 'range')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def move_slider_n_times_right(self, n: int) -> None:
        for _ in range(n):
            self.driver.find_element(*self.SLIDER).send_keys(Keys.ARROW_RIGHT)

    def get_slider_value(self) -> str:
        return self.driver.find_element(*self.SLIDER_VALUE).text
    