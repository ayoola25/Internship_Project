from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    ICON_BTN = (By.CSS_SELECTOR, "a[href='https://gettop.us/cart/']")
    PRODUCT = (By.XPATH, "//p[@class='name product-title']//a[@href='https://gettop.us/product/ipad/']")
    PRODUCT_LINK = (By.ID, 'menu-item-470')
    IPHONE_LINK = (By.XPATH, "//li[@id='menu-item-469']//a[@href='https://gettop.us/product-category/iphone/']")

    def hover_link(self):
        actions = ActionChains(self.driver)
        product = self.find_element(*self.PRODUCT_LINK)
        actions.move_to_element(product)
        actions.perform()

    def hover_iPhone(self):
        actions = ActionChains(self.driver)
        product = self.find_element(*self.IPHONE_LINK)
        actions.move_to_element(product)
        actions.perform()

    def verify_link(self):
        self.wait_for_element_appear(*self.PRODUCT_LINK)

    def click_on_cart_icon(self):
        self.click(*self.ICON_BTN)



