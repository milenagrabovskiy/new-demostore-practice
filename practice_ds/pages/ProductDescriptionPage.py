from practice_ds.locators.ProductDescriptionPageLocators import ProductDescriptionPageLocators


class ProductDescriptionPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_first_product(self):
        self.driver.get("https://demostore.supersqa.com/product/album/").click()

    def click_add_to_cart_btn(self):
        self.driver.find_element(*ProductDescriptionPageLocators.ADD_TO_CART_BTN).click()

    def click_add_coupon_btn(self):
        self.driver.find_element(*ProductDescriptionPageLocators.ADD_COUPON_BTN)
