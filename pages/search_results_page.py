from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")

    def verify_search_results(self, expected_result):
        self.verify_text(expected_result, *self.SEARCH_RESULT_TEXT)
