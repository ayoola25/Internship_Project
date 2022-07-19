from selenium.webdriver.common.by import By

from pages.base_page import Page


class BestsellersPage(Page):
    FIVE_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

    def open_bestsellers(self):
        self.open_page('gp/bestsellers/')

    def verify_links_present(self, expected_links):
        actual_links = self.driver.find_elements(*self.FIVE_LINKS)
        assert len(actual_links) == int(expected_links), \
            f'Expected! {expected_links} links, but got {len(actual_links)}'
