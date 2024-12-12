# UI Tests for the backpack product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, BackpackPage

def test_backpack_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Backpack')

  title = backpack_page.get_backpack_title()
  assert title == 'Sauce Labs Backpack'

def test_backpack_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['backpack'])

  title = backpack_page.get_backpack_title()
  assert title == product_titles['backpack']

def test_backpack_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  title = backpack_page.get_backpack_title()
  assert title == backpack_info['title']

def test_backpack_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  title = backpack_page.get_backpack_title()
  assert title == backpack_info['title']

def test_backpack_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Backpack')

  price = backpack_page.get_backpack_price()
  assert price == '$29.99'

def test_backpack_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['backpack'])

  price = backpack_page.get_backpack_price()
  assert price == product_prices['backpack']

def test_backpack_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  price = backpack_page.get_backpack_price()
  assert price == backpack_info['price']

def test_backpack_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  price = backpack_page.get_backpack_price()
  assert price == backpack_info['price']

def test_backpack_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  description = ("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with "
                 "unequaled laptop and tablet protection.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Backpack')

  page_description = backpack_page.get_backpack_description()
  assert description == page_description

def test_backpack_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['backpack'])

  page_description = backpack_page.get_backpack_description()
  assert page_description == product_descriptions['backpack']

def test_backpack_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  page_description = backpack_page.get_backpack_description()
  assert page_description == backpack_info['description']

def test_backpack_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  backpack_info = product_info['backpack']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(backpack_info['title'])

  page_description = backpack_page.get_backpack_description()
  assert page_description == backpack_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  backpack_page.click_add_to_cart_btn()

  remove_btn = backpack_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  backpack_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  backpack_page.click_add_to_cart_btn()
  remove_btn = backpack_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert backpack_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  backpack_page.click_add_to_cart_btn()
  remove_btn = backpack_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_backpack_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")

  assert backpack_page.get_backpack_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  backpack_page = BackpackPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  backpack_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'