# UI Tests for the bolt shirt product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, BoltShirtPage

def test_bolt_shirt_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bolt T-Shirt')

  title = bolt_shirt_page.get_bolt_shirt_title()
  assert title == 'Sauce Labs Bolt T-Shirt'

def test_bolt_shirt_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bolt_shirt'])

  title = bolt_shirt_page.get_bolt_shirt_title()
  assert title == product_titles['bolt_shirt']

def test_bolt_shirt_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  title = bolt_shirt_page.get_bolt_shirt_title()
  assert title == bolt_shirt_info['title']

def test_bolt_shirt_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  title = bolt_shirt_page.get_bolt_shirt_title()
  assert title == bolt_shirt_info['title']

def test_bolt_shirt_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bolt T-Shirt')

  price = bolt_shirt_page.get_bolt_shirt_price()
  assert price == '$15.99'

def test_bolt_shirt_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bolt_shirt'])

  price = bolt_shirt_page.get_bolt_shirt_price()
  assert price == product_prices['bolt_shirt']

def test_bolt_shirt_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  price = bolt_shirt_page.get_bolt_shirt_price()
  assert price == bolt_shirt_info['price']

def test_bolt_shirt_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  price = bolt_shirt_page.get_bolt_shirt_price()
  assert price == bolt_shirt_info['price']

def test_bolt_shirt_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  description = ("Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun "
                 "combed cotton, heather gray with red bolt.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bolt T-Shirt')

  page_description = bolt_shirt_page.get_bolt_shirt_description()
  assert description == page_description

def test_bolt_shirt_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bolt_shirt'])

  page_description = bolt_shirt_page.get_bolt_shirt_description()
  assert page_description == product_descriptions['bolt_shirt']

def test_bolt_shirt_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  page_description = bolt_shirt_page.get_bolt_shirt_description()
  assert page_description == bolt_shirt_info['description']

def test_bolt_shirt_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bolt_shirt_info = product_info['bolt_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bolt_shirt_info['title'])

  page_description = bolt_shirt_page.get_bolt_shirt_description()
  assert page_description == bolt_shirt_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")
  bolt_shirt_page.click_add_to_cart_btn()

  remove_btn = bolt_shirt_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")
  bolt_shirt_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")
  bolt_shirt_page.click_add_to_cart_btn()
  remove_btn = bolt_shirt_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert bolt_shirt_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")
  bolt_shirt_page.click_add_to_cart_btn()
  remove_btn = bolt_shirt_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_bolt_shirt_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")

  assert bolt_shirt_page.get_bolt_shirt_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bolt_shirt_page = BoltShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bolt T-Shirt")
  bolt_shirt_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'