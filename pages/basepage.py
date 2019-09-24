from selenium.common.exceptions import WebDriverException


class BasePage:
    """
    This is my Base Page
    """
    time_to_wait = 10
    url = 'https://www.google.com'

    def __init__(self, driver):
        """
        Instantiate driver
        """
        self.driver = driver

    def visit(self):
        """
        opne the URL
        """
        try:
            self.driver.get(self.url)
        except WebDriverException:
            print("Incorrect URL")
