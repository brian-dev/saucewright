# Functional login page tests. Runs both positive and negative tests cases along with
# a check for locked out user.

from pages import LoginPage
from tests.conftest import user_creds


def test_successful_login(page, user_creds):
    login_page = LoginPage(page)
    login_page.login(user_creds['standard_user'], user_creds['password'])

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_invalid_username_and_password(page):
    login_page = LoginPage(page)

    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_invalid_username(page, user_creds):
    login_page = LoginPage(page)

    login_page.login("invalid_user", user_creds['password'])
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_invalid_password(page, user_creds):
    login_page = LoginPage(page)

    login_page.login(user_creds['standard_user'], 'password')
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_empty_username(page, user_creds):
    login_page = LoginPage(page)

    login_page.login("", user_creds['password'])
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username is required"


def test_empty_password(page, user_creds):
    login_page = LoginPage(page)

    login_page.login(user_creds['standard_user'], "")
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Password is required"


def test_empty_username_and_password(page):
    login_page = LoginPage(page)

    login_page.login("", "")
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username is required"


def test_locked_out_user(page, user_creds):
    login_page = LoginPage(page)

    login_page.login(user_creds['locked_user'], user_creds['password'])
    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Sorry, this user has been locked out."
