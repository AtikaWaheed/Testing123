from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class IntroCOde(BasePage):

    url = "https://www.google.com/"

    def is_browser_on_page(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchform"))
        )

    def find_search_bar(self):
        search_field = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']"))
        )
        search_field.send_keys('CoreAcademy')
        search_field.send_keys(Keys.ENTER)




