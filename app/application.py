from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.cart_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.page = Page(self.driver)

