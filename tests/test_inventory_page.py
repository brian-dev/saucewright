# UI tests for the all inventory page. Runs checks to ensure items and elements
# are displayed on screen. All tests performed with the standard user credentials.
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, CartAction


# Validates that the expected number of product cards are displayed on screen
# by counting the number of inventory items on page
def test_all_cards_displayed(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])

    assert inv_page.get_product_card_count() == 6

# Validates all expected product titles are on page by defining a list
# in the test and validating that value is in a list generated by scraping
# the titles from the page
def test_all_titles_displayed_list(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)
    title_list = [
        'Sauce Labs Backpack',
        'Sauce Labs Bike Light',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Fleece Jacket',
        'Sauce Labs Onesie',
        'Test.allTheThings() T-Shirt (Red)'
    ]

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for title in title_list:
        assert inv_page.check_title_displayed(title) is True

# Validates all expected product titles are on page by reading from a dictionary defined
# as a fixture then validating the value from the fixture is included in a list
# generated by scraping the titles from the page
def test_all_titles_displayed_fixture(page, user_creds, product_titles):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for key, value in product_titles.items():
        assert value in inv_page.get_product_titles()

# Validates all expected product titles are on page by reading from a list defined
# in a yaml file then validating the value from the yaml list is included in a list
# generated by scraping the titles from the page
def test_all_titles_displayed_yml(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.yml', 'r') as file:
        titles_list = yaml.safe_load(file)

    titles = titles_list['product_titles']
    for title in titles:
        assert title in inv_page.get_product_titles()

# Validates all expected product titles are on page by reading from a list defined
# in a json file then validating the value from the json list is included in a list
# generated by scraping the titles from the page
def test_all_titles_displayed_json(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.json', 'r') as file:
        titles_list = json.load(file)

    titles = titles_list['titles']
    for title in titles:
        assert title in inv_page.get_product_titles()

# Validates all expected product descriptions are on page by defining a list
# in the test and validating that value is in a list generated by scraping
# the descriptions from the page
def test_all_descriptions_displayed_list(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)
    desc_list = [
        "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled "
        "laptop and tablet protection.",
        "A red light isn't the desired state in testing but it sure helps when riding your bike at night. "
        "Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed "
        "cotton, heather gray with red bolt.",
        "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything "
        "from a relaxing day outdoors to a busy day at the office.",
        "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, "
        "two-needle hemmed sleeved and bottom won't unravel.",
        "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. "
        "Super-soft and comfy ringspun combed cotton."
    ]

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for desc in desc_list:
        assert inv_page.check_description_displayed(desc) is True

# Validates all expected product descriptions are on page by reading from a dictionary defined
# as a fixture then validating the value from the fixture is included in a list
# generated by scraping the descriptions from the page
def test_all_descriptions_displayed_fixture(page, user_creds, product_descriptions):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for key, value in product_descriptions.items():
        assert value in inv_page.get_product_descriptions()

# Validates all expected product descriptions are on page by reading from a list defined
# in a yaml file then validating the value from the yaml list is included in a list
# generated by scraping the descriptions from the page
def test_all_descriptions_displayed_yml(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.yml', 'r') as file:
        descriptions_list = yaml.safe_load(file)

    descriptions = descriptions_list['product_descriptions']
    for description in descriptions:
        assert description in inv_page.get_product_descriptions()

# Validates all expected product descriptions are on page by reading from a list defined
# in a json file then validating the value from the json list is included in a list
# generated by scraping the descriptions from the page
def test_all_descriptions_displayed_json(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.json', 'r') as file:
        descriptions_list = json.load(file)

    descriptions = descriptions_list['descriptions']
    for description in descriptions:
        assert description in inv_page.get_product_descriptions()

# Validates all expected product prices are on page by defining a list
# in the test and validating that value is in a list generated by scraping
# the prices from the page
def test_all_prices_displayed_list(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)
    price_list = [
        '$29.99',
        '$9.99',
        '$15.99',
        '$49.99',
        '$7.99'
    ]

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for price in price_list:
        assert inv_page.check_price_displayed(price) is True

# Validates all expected product prices are on page by reading from a dictionary defined
# as a fixture then validating the value from the fixture is included in a list
# generated by scraping the prices from the page
def test_all_prices_displayed_fixture(page, user_creds, product_prices):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    for key, value in product_prices.items():
        assert value in inv_page.get_product_prices()

# Validates all expected product prices are on page by reading from a list defined
# in a yaml file then validating the value from the yaml list is included in a list
# generated by scraping the prices from the page
def test_all_prices_displayed_yml(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.yml', 'r') as file:
        prices_list = yaml.safe_load(file)

    prices = prices_list['product_prices']
    for price in prices:
        assert price in inv_page.get_product_prices()

# Validates all expected product prices are on page by reading from a list defined
# in a json file then validating the value from the json list is included in a list
# generated by scraping the prices from the page
def test_all_prices_displayed_json(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    with open('product_info.json', 'r') as file:
        prices_list = json.load(file)

    prices = prices_list['prices']
    for price in prices:
        assert price in inv_page.get_product_prices()

# Validates cart badge count matches the expected count when all cart items are added to the cart by
# iterating over the list of add to cart buttons, clicking them, then collecting the value from the
# cart badge displayed on screen
def test_add_to_cart_list(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.add_all_items_to_cart()
    assert inv_page.get_cart_badge_count() == "6"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_backpack_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_backpack_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_bike_light_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_bike_light_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_bolt_shirt_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_bolt_shirt_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_jacket_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_jacket_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_onesie_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_onesie_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"

# Validates the cart badge updates to the correct count when the item is added to the cart
# via the add to cart button on the inventory card
def test_add_test_shirt_to_cart(page, user_creds):
    login_page = LoginPage(page)
    inv_page = InventoryPage(page)

    login_page.login(user_creds['standard_user'], user_creds['password'])
    inv_page.modify_test_shirt_cart(CartAction.ADD)
    assert inv_page.get_cart_badge_count() == "1"
