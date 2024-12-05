# UI tests for the all inventory page. Runs checks to ensure items and elements
# are displayed on screen.
import pytest
from pages import LoginPage, InventoryPage


def test_all_cards_displayed(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])

    assert inv_page.get_product_card_count() == 6

@pytest.mark.test
def test_all_titles_displayed(page, user_creds, product_titles):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.get_product_titles()
