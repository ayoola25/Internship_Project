from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


# class SignInPage(Page):
#     ERROR_MSG = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")
#     invalid_credentials = 'Having trouble signing in? Confirm the phone number associated with your account to enter the app'
#
#     def verify_error(self, error_type):
#         if error_type == 'invalid_credentials':
#             self.verify_text(self.invalid_credentials, *self.ERROR_MSG)
#         elif error_type == 'Password is required':
#             self.verify_text(self.invalid_credentials, *self.ERROR_MSG)
