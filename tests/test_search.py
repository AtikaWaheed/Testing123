from tests.basetests import BaseTests
from pages.intro_code import IntroCOde
from pages.resultpage import ResultPage


class SearchTest(BaseTests):

    def setUp(self):
        super(SearchTest, self).setUp()
        self.intro_code = IntroCOde(self.driver)
        self.result_page = ResultPage(self.driver)

    def test_search(self):
        self.intro_code.visit()
        self.intro_code.is_browser_on_page()
        self.intro_code.find_search_bar()
        self.result_page.is_browser_on_page()

