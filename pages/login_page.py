from playwright.sync_api import Page


class LoginPage:
    USERNAME_INPUT = "[data-test= 'username']"
    PASSWORD_INPUT = "[data-test= 'password']"
    LOGIN_BTN = "[data-test= 'login-button']"
    ERROR_MESSAGE = "[data-test= 'error']"

    def __init__(self, page: Page):
        self.page = page

    def enter_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.page.click(self.LOGIN_BTN)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.page.inner_text(self.ERROR_MESSAGE)