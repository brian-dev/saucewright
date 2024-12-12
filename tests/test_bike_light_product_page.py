# UI Tests for the bike light product page
import json
import pytest
import yaml
from pages import LoginPage, InventoryPage, BikeLightPage

def test_bike_light_title_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bike Light')

  title = bike_light_page.get_bike_light_title()
  assert title == 'Sauce Labs Bike Light'

def test_bike_light_title_fixture(page, user_creds, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bike_light'])

  title = bike_light_page.get_bike_light_title()
  assert title == product_titles['bike_light']

def test_bike_light_title_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  title = bike_light_page.get_bike_light_title()
  assert title == bike_light_info['title']

def test_bike_light_title_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  title = bike_light_page.get_bike_light_title()
  assert title == bike_light_info['title']

def test_bike_light_price_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bike Light')

  price = bike_light_page.get_bike_light_price()
  assert price == '$9.99'

def test_bike_light_price_fixture(page, user_creds, product_prices, product_titles):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bike_light'])

  price = bike_light_page.get_bike_light_price()
  assert price == product_prices['bike_light']

def test_bike_light_price_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  price = bike_light_page.get_bike_light_price()
  assert price == bike_light_info['price']

def test_bike_light_price_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  price = bike_light_page.get_bike_light_price()
  assert price == bike_light_info['price']

def test_bike_light_description_hardcoded(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  description = ("A red light isn't the desired state in testing but it sure helps when riding your bike at night. "
                 "Water-resistant with 3 lighting modes, 1 AAA battery included.")

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title('Sauce Labs Bike Light')

  page_description = bike_light_page.get_bike_light_description()
  assert description == page_description

def test_bike_light_description_fixture(page, user_creds, product_titles, product_descriptions):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(product_titles['bike_light'])

  page_description = bike_light_page.get_bike_light_description()
  assert page_description == product_descriptions['bike_light']

def test_bike_light_description_yml(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.yml', 'r') as file:
    product_info = yaml.safe_load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  page_description = bike_light_page.get_bike_light_description()
  assert page_description == bike_light_info['description']

def test_bike_light_description_json(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)
  with open('product_info.json', 'r') as file:
    product_info = json.load(file)
  bike_light_info = product_info['bike_light']

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title(bike_light_info['title'])

  page_description = bike_light_page.get_bike_light_description()
  assert page_description == bike_light_info['description']

def test_add_to_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bike Light")
  bike_light_page.click_add_to_cart_btn()

  remove_btn = bike_light_page.get_remove_from_cart_btn()
  assert remove_btn.is_visible()

def test_add_to_cart_badge_count(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Backpack")
  bike_light_page.click_add_to_cart_btn()

  cart_count = inv_page.get_cart_badge_count()
  assert cart_count == "1"

def test_remove_from_cart_btn_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bike Light")
  bike_light_page.click_add_to_cart_btn()
  remove_btn = bike_light_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert bike_light_page.get_add_to_cart_btn().is_visible()

def test_remove_from_cart_badge_count_update(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bike Light")
  bike_light_page.click_add_to_cart_btn()
  remove_btn = bike_light_page.get_remove_from_cart_btn()
  if remove_btn.is_visible():
    remove_btn.click()
  else:
    raise "Remove button was not visible"

  assert inv_page.get_cart_badge().is_visible() is False

def test_bike_light_img_displayed(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bike Light")

  assert bike_light_page.get_bike_light_img().is_visible()

def test_back_to_products_nav(page, user_creds):
  login_page = LoginPage(page)
  inv_page = InventoryPage(page)
  bike_light_page = BikeLightPage(page)

  login_page.login(user_creds['standard_user'], user_creds['password'])
  inv_page.click_on_item_title("Sauce Labs Bike Light")
  bike_light_page.click_back_to_products_btn()

  assert page.url == 'https://www.saucedemo.com/inventory.html'