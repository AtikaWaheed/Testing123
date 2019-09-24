from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage(BasePage):

    def is_browser_on_page(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchform"))
        )
