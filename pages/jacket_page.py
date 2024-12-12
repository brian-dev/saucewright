from playwright.sync_api import Page


class JacketPage:
    BACK_TO_PRODUCTS_BTN = "[data-test = 'back-to-products']"
    JACKET_IMG = "[data-test = 'item-sauce-labs-fleece-jacket-img']"
    JACKET_TITLE = "[data-test = 'inventory-item-name']"
    JACKET_DESCRIPTION = "[data-test = 'inventory-item-desc']"
    JACKET_PRICE = "[data-test = 'inventory-item-price']"
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

    def get_jacket_img(self):
        return self.page.locator(self.JACKET_IMG)

    def get_jacket_title(self):
        title = self.page.locator(self.JACKET_TITLE)
        return title.inner_text()

    def get_jacket_description(self):
        desc = self.page.locator(self.JACKET_DESCRIPTION)
        return desc.inner_text()

    def get_jacket_price(self):
        price = self.page.locator(self.JACKET_PRICE)
        return price.inner_text()

    def get_remove_from_cart_btn(self):
        return self.page.locator(self.REMOVE_FROM_CART_BTN)

    def get_add_to_cart_btn(self):
        return self.page.locator(self.ADD_TO_CART_BTN)