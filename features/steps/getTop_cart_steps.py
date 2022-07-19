from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ICON_BTN = (By.CSS_SELECTOR, "a[href='https://gettop.us/cart/']")


@when('click on cart_icon')
def click_on(context):
    # context.driver.find_element(*ICON_BTN).click()
    context.app.header.click_on_cart_icon()


@then('Verify Your cart is currently empty text present')
def verify_gitTopCart_empty(context):
    # context.driver.wait.until(EC.url_contains('https://www.'))
    context.app.cart_page.verify_gitTopCart_empty()



