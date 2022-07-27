from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    # EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.cart-empty.woocommerce-info')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.woocommerce-mini-cart__empty-message')  # for Mobile Web test

    def verify_getTopCart_empty(self):
        # self.verify_text('Your cart is currently empty.', *self.EMPTY_CART_TEXT)
        self.verify_text('No products in the cart.', *self.EMPTY_CART_TEXT)  # for Mobile Web test
