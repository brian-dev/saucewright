from enum import Enum
from playwright.sync_api import Page

class CartAction(Enum):
    ADD = "add"
    REMOVE = "remove"

class InventoryPage:
    # Product card element locators
    PRODUCT_CARDS = "[data-test = 'inventory-item']"
    PRODUCT_TITLES = "[data-test = 'inventory-item-name']"
    PRODUCT_DESCRIPTIONS = "[data-test = 'inventory-item-desc']"
    PRODUCT_PRICES = "[data-test = 'inventory-item-price']"
    # Locators to add an item to the cart
    BACKPACK_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-sauce-labs-backpack']"
    BIKE_LIGHT_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-sauce-labs-bike-light']"
    BOLT_SHIRT_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-sauce-labs-bolt-t-shirt']"
    JACKET_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-sauce-labs-fleece-jacket']"
    ONESIE_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-sauce-labs-onesie']"
    TEST_SHIRT_ADD_TO_CART_BTN = "[data-test = 'add-to-cart-test.allthethings()-t-shirt-(red)']"
    # Locators to remove an item from the cart
    BACKPACK_REMOVE_FROM_CART_BTN = "[data-test = 'remove-sauce-labs-backpack']"
    BIKE_LIGHT_REMOVE_FROM_CART_BTN = "[data-test = 'remove-sauce-labs-bike-light']"
    BOLT_SHIRT_REMOVE_FROM_CART_BTN = "[data-test = 'remove-sauce-labs-bolt-t-shirt']"
    JACKET_REMOVE_FROM_CART_BTN = "[data-test = 'remove-sauce-labs-fleece-jacket']"
    ONESIE_REMOVE_FROM_CART_BTN = "[data-test = 'remove-sauce-labs-onesie']"
    TEST_SHIRT_REMOVE_FROM_CART_BTN = "[data-test = 'remove-test.allthethings()-t-shirt-(red)']"
    # Additional locators for page elements
    MENU_BTN = "[data-test = 'open-menu']"
    CART_BTN = "[data-test = 'shopping-cart-link']"
    CART_BADGE = "[data-test = 'shopping-cart-badge']"
    PRODUCT_SORT_DROPDOWN = "[data-test = 'product-sort-container']"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_inventory_page(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_product_cards(self):
        return self.PRODUCT_CARDS

    def get_product_titles(self):
        return self.page.inner_text(self.PRODUCT_TITLES)

    def get_product_descriptions(self):
        return self.page.inner_text(self.PRODUCT_DESCRIPTIONS)

    def get_product_prices(self):
        return self.PRODUCT_PRICES

    def check_title_displayed(self, product_name):
        titles = self.get_product_titles()
        displayed = False

        if product_name in titles:
            displayed = True
        return displayed

    def check_description_displayed(self, product_description):
        descriptions = self.get_product_descriptions()
        displayed = False

        if product_description in descriptions:
            displayed = True
        return displayed

    def modify_backpack_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.BACKPACK_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.BACKPACK_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def modify_bike_light_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.BIKE_LIGHT_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.BIKE_LIGHT_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def modify_bolt_shirt_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.BOLT_SHIRT_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.BOLT_SHIRT_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def modify_jacket_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.JACKET_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.JACKET_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def modify_onesie_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.ONESIE_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.ONESIE_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def modify_test_shirt_cart(self, action: CartAction):
        if action == CartAction.ADD:
            self.page.click(self.TEST_SHIRT_ADD_TO_CART_BTN)
        elif action == CartAction.REMOVE:
            self.page.click(self.TEST_SHIRT_REMOVE_FROM_CART_BTN)
        else:
            raise ValueError("Invalid action specified. Use Action.ADD or Action.REMOVE.")

    def open_menu(self):
        self.page.click(self.MENU_BTN)

    def open_cart(self):
        self.page.click(self.CART_BTN)

