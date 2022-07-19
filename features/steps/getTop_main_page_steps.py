from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRODUCT_LINK = (By.ID, 'menu-item-470')
PRODUCT = (By.XPATH, "//p[@class='name product-title']//a[@href='https://gettop.us/product/ipad/']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[type='submit'][name='add-to-cart']")
IPAD = (By.XPATH, "//li[@id='menu-item-390']//a[@href='https://gettop.us/product/ipad/']")
CART = (By.CSS_SELECTOR, "[class='cart-icon image-icon']")
IPHONE_12 = (By.XPATH, "//li[@id='menu-item-484']//a[@href='#']")


@given('Open GitTop page')
def open_amazon(context):
    # context.driver.get('https://gettop.us/')
    context.app.main_page.open_main_page()


@when('Click on Product Link')
def click_product_link(context):
    context.driver.find_element(*PRODUCT_LINK).click()


@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT).click()


@when('Click on iPad')
def click_iPad(context):
    context.driver.find_element(*IPAD).click()


@when('Click on iPhone 12 button')
def click_iPhone(context):
    context.driver.find_element(*IPHONE_12).click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    # context.driver.wait.until(EC.invisibility_of_element_located(ADD_TO_CART_BUTTON))


@when('Open View Cart page')
def view_cart_page(context):
    context.driver.get('https://gettop.us/cart/')


@when('Hover over IPAD link')
def hover_link(context):
    context.app.header.hover_link()


@when('Hover over IPHONE link')
def hover_iPhone(context):
    context.app.header.hover_iPhone()


@then('Verify IPAD link is selected')
def verify_link(context):
    context.app.header.verify_link()


@then('Verify user can click iPhone 12 button')
def verify_click_iPhone12(context):
    context.driver.wait.until(EC.url_contains('https://gettop.us/product/ipad/'), 'iPhone 12 btn not clickable')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == \
           actual_text, f'Expected! {expected_count} but got {actual_text}'


