from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.pages.abstract import AbstractPage

class DropdownPage(AbstractPage):

    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def __find_dropdown_element(self) -> Select:
        return Select(self.driver.find_element(*self.DROPDOWN))

    def select_dropdown_option(self, option_name: str) -> None:
        select = self.__find_dropdown_element()
        select.select_by_visible_text(option_name)

    def get_active_dropdown_option(self) -> list:
        return self.__find_dropdown_element().first_selected_option.text
