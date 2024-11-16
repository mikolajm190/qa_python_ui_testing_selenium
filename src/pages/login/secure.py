from selenium.webdriver.common.by import By

from src.pages.abstract import AbstractPage

class SecureAreaPage(AbstractPage):
    
    BANNER = (By.ID, 'flash')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_banner_text(self) -> str:
        return self.driver.find_element(*self.BANNER).text