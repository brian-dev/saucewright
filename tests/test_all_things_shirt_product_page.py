# UI Tests for the test shirt product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, AllThingsShirtPage

def test_all_things_shirt_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Test.allTheThings() T-Shirt (Red)')

  title = all_things_shirt_page.get_all_things_shirt_title()
  assert title == 'Test.allTheThings() T-Shirt (Red)'

def test_all_things_shirt_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['all_things_shirt'])

  title = all_things_shirt_page.get_all_things_shirt_title()
  assert title == product_titles['all_things_shirt']

def test_all_things_shirt_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  title = all_things_shirt_page.get_all_things_shirt_title()
  assert title == all_things_shirt_info['title']

def test_all_things_shirt_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  title = all_things_shirt_page.get_all_things_shirt_title()
  assert title == all_things_shirt_info['title']

def test_all_things_shirt_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Test.allTheThings() T-Shirt (Red)')

  price = all_things_shirt_page.get_all_things_shirt_price()
  assert price == '$15.99'

def test_all_things_shirt_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['all_things_shirt'])

  price = all_things_shirt_page.get_all_things_shirt_price()
  assert price == product_prices['all_things_shirt']

def test_all_things_shirt_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  price = all_things_shirt_page.get_all_things_shirt_price()
  assert price == all_things_shirt_info['price']

def test_all_things_shirt_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  price = all_things_shirt_page.get_all_things_shirt_price()
  assert price == all_things_shirt_info['price']

def test_all_things_shirt_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  description = ("This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a "
                 "few tests. Super-soft and comfy ringspun combed cotton.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Test.allTheThings() T-Shirt (Red)')

  page_description = all_things_shirt_page.get_all_things_shirt_description()
  assert description == page_description

def test_all_things_shirt_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['all_things_shirt'])

  page_description = all_things_shirt_page.get_all_things_shirt_description()
  assert page_description == product_descriptions['all_things_shirt']

def test_all_things_shirt_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  page_description = all_things_shirt_page.get_all_things_shirt_description()
  assert page_description == all_things_shirt_info['description']

def test_all_things_shirt_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  all_things_shirt_info = product_info['all_things_shirt']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(all_things_shirt_info['title'])

  page_description = all_things_shirt_page.get_all_things_shirt_description()
  assert page_description == all_things_shirt_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")
  all_things_shirt_page.click_add_to_cart_btn()

  remove_btn = all_things_shirt_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")
  all_things_shirt_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")
  all_things_shirt_page.click_add_to_cart_btn()
  remove_btn = all_things_shirt_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert all_things_shirt_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")
  all_things_shirt_page.click_add_to_cart_btn()
  remove_btn = all_things_shirt_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_all_things_shirt_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")

  assert all_things_shirt_page.get_all_things_shirt_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  all_things_shirt_page = AllThingsShirtPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Test.allTheThings() T-Shirt (Red)")
  all_things_shirt_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'