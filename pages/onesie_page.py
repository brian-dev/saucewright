from playwright.sync_api import Page


class OnesiePage:
    BACK_TO_PRODUCTS_BTN = "[data-test = 'back-to-products']"
    ONESIE_IMG = "[data-test = 'item-sauce-labs-onesie-img']"
    ONESIE_TITLE = "[data-test = 'inventory-item-name']"
    ONESIE_DESCRIPTION = "[data-test = 'inventory-item-desc']"
    ONESIE_PRICE = "[data-test = 'inventory-item-price']"
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

    def get_onesie_img(self):
        return self.page.locator(self.ONESIE_IMG)

    def get_onesie_title(self):
        title = self.page.locator(self.ONESIE_TITLE)
        return title.inner_text()

    def get_onesie_description(self):
        desc = self.page.locator(self.ONESIE_DESCRIPTION)
        return desc.inner_text()

    def get_onesie_price(self):
        price = self.page.locator(self.ONESIE_PRICE)
        return price.inner_text()

    def get_remove_from_cart_btn(self):
        return self.page.locator(self.REMOVE_FROM_CART_BTN)

    def get_add_to_cart_btn(self):
        return self.page.locator(self.ADD_TO_CART_BTN)