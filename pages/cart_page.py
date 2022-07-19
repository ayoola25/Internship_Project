from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.cart-empty.woocommerce-info')

    def verify_gitTopCart_empty(self):
        self.verify_text('Your cart is currently empty.', *self.EMPTY_CART_TEXT)
