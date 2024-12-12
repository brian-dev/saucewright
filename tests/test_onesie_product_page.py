# UI Tests for the onesie product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, OnesiePage

def test_onesie_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Onesie')

  title = onesie_page.get_onesie_title()
  assert title == 'Sauce Labs Onesie'

def test_onesie_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['onesie'])

  title = onesie_page.get_onesie_title()
  assert title == product_titles['onesie']

def test_onesie_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  title = onesie_page.get_onesie_title()
  assert title == onesie_info['title']

def test_onesie_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  title = onesie_page.get_onesie_title()
  assert title == onesie_info['title']

def test_onesie_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Onesie')

  price = onesie_page.get_onesie_price()
  assert price == '$7.99'

def test_onesie_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['onesie'])

  price = onesie_page.get_onesie_price()
  assert price == product_prices['onesie']

def test_onesie_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  price = onesie_page.get_onesie_price()
  assert price == onesie_info['price']

def test_onesie_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  price = onesie_page.get_onesie_price()
  assert price == onesie_info['price']

def test_onesie_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  description = ("Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom "
                 "closure, two-needle hemmed sleeved and bottom won't unravel.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Onesie')

  page_description = onesie_page.get_onesie_description()
  assert description == page_description

def test_onesie_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['onesie'])

  page_description = onesie_page.get_onesie_description()
  assert page_description == product_descriptions['onesie']

def test_onesie_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  page_description = onesie_page.get_onesie_description()
  assert page_description == onesie_info['description']

def test_onesie_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  onesie_info = product_info['onesie']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(onesie_info['title'])

  page_description = onesie_page.get_onesie_description()
  assert page_description == onesie_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")
  onesie_page.click_add_to_cart_btn()

  remove_btn = onesie_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")
  onesie_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")
  onesie_page.click_add_to_cart_btn()
  remove_btn = onesie_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert onesie_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")
  onesie_page.click_add_to_cart_btn()
  remove_btn =onesie_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_onesie_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")

  assert onesie_page.get_onesie_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  onesie_page = OnesiePage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Onesie")
  onesie_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'