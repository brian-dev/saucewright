from playwright.sync_api import Page


class AllThingsShirtPage:
    BACK_TO_PRODUCTS_BTN = "[data-test = 'back-to-products']"
    ALL_THINGS_SHIRT_IMG = "[data-test = 'item-test.allthethings()-t-shirt-(red)-img']"
    ALL_THINGS_SHIRT_TITLE = "[data-test = 'inventory-item-name']"
    ALL_THINGS_SHIRT_DESCRIPTION = "[data-test = 'inventory-item-desc']"
    ALL_THINGS_SHIRT_PRICE = "[data-test = 'inventory-item-price']"
    ADD_TO_CART_BTN = "[data-test = 'add-to-cart']"
    REMOVE_FROM_CART_BTN = "[data-test = 'remove']"

    def __init__(self, page: Page):
        self.page = page

    def click_back_to_products_btn(self):
        self.page.click(self.BACK_TO_PRODUCTS_BTN)

    def click_add_to_cart_btn(self):
        self.page.click(self.ADD_TO_CART_BTN)

    def click_remove_from_cart_btn(self):
        self.page.click(self.REMOVE_FROM_CART_BTN)

    def get_all_things_shirt_img(self):
        return self.page.locator(self.ALL_THINGS_SHIRT_IMG)

    def get_all_things_shirt_title(self):
        title = self.page.locator(self.ALL_THINGS_SHIRT_TITLE)
        return title.inner_text()

    def get_all_things_shirt_description(self):
        desc = self.page.locator(self.ALL_THINGS_SHIRT_DESCRIPTION)
        return desc.inner_text()

    def get_all_things_shirt_price(self):
        price = self.page.locator(self.ALL_THINGS_SHIRT_PRICE)
        return price.inner_text()

    def get_remove_from_cart_btn(self):
        return self.page.locator(self.REMOVE_FROM_CART_BTN)

    def get_add_to_cart_btn(self):
        return self.page.locator(self.ADD_TO_CART_BTN)