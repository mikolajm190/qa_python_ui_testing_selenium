import selenium.webdriver.remote.webdriver

class AbstractPage:

    def __init__(self, driver: selenium.webdriver.Remote) -> None:
        self.driver = driver