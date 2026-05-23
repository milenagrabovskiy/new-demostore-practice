import time

import pytest

from practice_ds.pages.CartPage import CartPage
from practice_ds.pages.HomePage import HomePage

import logging

from practice_ds.pages.ProductDescriptionPage import ProductDescriptionPage

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("init_driver", "setup")
class TestCouponCodes:

    FREE_COUPON = "SSQA100"

    @pytest.fixture(autouse=True)
    def setup(self):
        self.homepage = HomePage(self.driver)
        self.homepage.go_to_home_page()
        self.pdp = ProductDescriptionPage(self.driver)
        self.cartpage = CartPage(self.driver)


    @pytest.mark.test1
    def test_100_off_coupon(self):

        self.homepage.click_on_first_product()
        self.pdp.click_add_to_cart_btn()
        self.cartpage.go_to_cart_page()
        time.sleep(5)
        self.cartpage.click_add_coupon_btn()
        time.sleep(5)
        self.cartpage.input_coupon_code(self.FREE_COUPON)
        time.sleep(5)
        self.cartpage.click_add_coupon_btn()
        time.sleep(5)
        assert self.cartpage.get_cart_total() == "$0.00", (f"Unexpected cart total. Expected: $0.00, "
                                                          f"Actual: {self.cartpage.get_cart_total()}")

