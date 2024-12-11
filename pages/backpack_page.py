from playwright.sync_api import Page


class BackpackPage:
    BACK_TO_PRODUCTS_BTN = "[data-test = 'back-to-products']"
    BACKPACK_IMG = "[data-test = 'item-sauce-labs-backpack-img']"
    BACKPACK_TITLE = "[data-test = 'inventory-item-name']"
    BACKPACK_DESCRIPTION = "[data-test = 'inventory-item-desc']"
    BACKPACK_PRICE = "[data-test = 'inventory-item-price']"
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

    def get_backpack_img(self):
        return self.page.locator(self.BACKPACK_IMG)

    def get_backpack_title(self):
        title = self.page.locator(self.BACKPACK_TITLE)
        return title.inner_text()

    def get_backpack_description(self):
        desc = self.page.locator(self.BACKPACK_DESCRIPTION)
        return desc.inner_text()

    def get_backpack_price(self):
        price = self.page.locator(self.BACKPACK_PRICE)
        return price.inner_text()

    def get_remove_from_cart_btn(self):
        return self.page.locator(self.REMOVE_FROM_CART_BTN)

    def get_add_to_cart_btn(self):
        return self.page.locator(self.ADD_TO_CART_BTN)