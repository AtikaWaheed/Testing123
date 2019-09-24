import unittest
from selenium import webdriver


class BaseTests(unittest.TestCase):
    """
    This is test class
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
