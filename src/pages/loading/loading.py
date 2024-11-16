from selenium.webdriver.common.by import By

from src.pages.abstract import AbstractPage
from src.pages.loading.dynamic_loading import DynamicLoadingPage

class LoadingPage(AbstractPage):

    DYNAMIC_LOADING_LINK = (By.XPATH, ".//a[contains(text(), 'Example 1')]")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_on_dynamic_loading_link(self) -> DynamicLoadingPage:
        self.driver.find_element(*self.DYNAMIC_LOADING_LINK).click()
        return DynamicLoadingPage(self.driver)
