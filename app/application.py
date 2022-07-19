from pages.article_page import ArticlePage
from pages.base_page import Page
from pages.bestsellers_page import BestsellersPage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.no_search_results_page import NoSearchResults
from pages.right_navigation import RightNavigation
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.article_page = ArticlePage(self.driver)
        self.bestsellers_page = BestsellersPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.no_search_results_page = NoSearchResults(self.driver)
        self.page = Page(self.driver)
        self.right_navigation = RightNavigation(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = SignInPage(self.driver)
