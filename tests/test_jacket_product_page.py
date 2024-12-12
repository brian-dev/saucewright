# UI Tests for the backpack product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, JacketPage

def test_jacket_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Fleece Jacket')

  title = jacket_page.get_jacket_title()
  assert title == 'Sauce Labs Fleece Jacket'

def test_jacket_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['jacket'])

  title = jacket_page.get_jacket_title()
  assert title == product_titles['jacket']

def test_jacket_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  title =jacket_page.get_jacket_title()
  assert title == jacket_info['title']

def test_jacket_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  title = jacket_page.get_jacket_title()
  assert title == jacket_info['title']

def test_jacket_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Fleece Jacket')

  price = jacket_page.get_jacket_price()
  assert price == '$49.99'

def test_jacket_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['jacket'])

  price = jacket_page.get_jacket_price()
  assert price == product_prices['jacket']

def test_jacket_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  price = jacket_page.get_jacket_price()
  assert price == jacket_info['price']

def test_jacket_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  price = jacket_page.get_jacket_price()
  assert price == jacket_info['price']

def test_jacket_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  description = ("It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling "
                 "everything from a relaxing day outdoors to a busy day at the office.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Fleece Jacket')

  page_description = jacket_page.get_jacket_description()
  assert description == page_description

def test_jacket_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['jacket'])

  page_description = jacket_page.get_jacket_description()
  assert page_description == product_descriptions['jacket']

def test_jacket_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  page_description = jacket_page.get_jacket_description()
  assert page_description == jacket_info['description']

def test_jacket_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  jacket_info = product_info['jacket']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(jacket_info['title'])

  page_description = jacket_page.get_jacket_description()
  assert page_description == jacket_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")
  jacket_page.click_add_to_cart_btn()

  remove_btn = jacket_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")
  jacket_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")
  jacket_page.click_add_to_cart_btn()
  remove_btn = jacket_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert jacket_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")
  jacket_page.click_add_to_cart_btn()
  remove_btn = jacket_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_jacket_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")

  assert jacket_page.get_jacket_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  jacket_page = JacketPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Fleece Jacket")
  jacket_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'