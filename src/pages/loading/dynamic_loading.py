from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.abstract import AbstractPage

class DynamicLoadingPage(AbstractPage):

    START_BUTTON = (By.TAG_NAME, "button")
    LOADING_ELEMENT = (By.CSS_SELECTOR, "#finish > h4")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_on_start_button(self) -> None:
        self.driver.find_element(*self.START_BUTTON).click()

    def get_loading_element_text(self) -> str:
        element = WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(self.LOADING_ELEMENT)
        )
        return element.text