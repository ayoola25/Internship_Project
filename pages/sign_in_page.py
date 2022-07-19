from pages.base_page import Page


class SignInPage(Page):
    def verify_signin_page_is_opened(self):
        self.verify_url_contains_query('ap/signin')
