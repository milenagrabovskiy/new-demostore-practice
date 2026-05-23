import pytest
import practice_ds.locators.HomePageLocators
from practice_ds.locators.HomePageLocators import HomePageLocators


class HomePage:

    URL = "https://demostore.supersqa.com/"

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.URL)

    def get_all_products(self):
        return self.driver.find_elements(*HomePageLocators.ALL_PRODUCTS)

    def click_on_first_product(self):
        self.get_all_products()[0].click()