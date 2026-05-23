import time

from selenium.webdriver import Keys

from practice_ds.locators.CartPageLocators import CartPageLocators
from practice_ds.locators.HomePageLocators import HomePageLocators


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_page(self):
        self.driver.find_element(*HomePageLocators.CART_BTN).click()

    def click_add_coupon_btn(self):
        self.driver.find_element(*CartPageLocators.ADD_COUPON_BTN).click()

    def input_coupon_code(self, coupon_code):
        coupon_input = (self.driver.find_element(*CartPageLocators.COUPON_INPUT_FIELD))
        coupon_input.send_keys(coupon_code)
        coupon_input.send_keys(Keys.ENTER)

    def click_apply_coupon_btn(self):
        self.driver.find_element(*CartPageLocators.APPLY_COUPON_BTN).click()
        # time.sleep(2)
        # self.driver.find_element(*CartPageLocators.APPLY_COUPON_BTN).click()

    def get_cart_total(self):
        return self.driver.find_element(*CartPageLocators.CART_TOTAL).text
