
import logging

import pytest

from practice_ds.pages.HomePage import HomePage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("init_driver", "setup")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.homepage = HomePage(self.driver)
        self.homepage.go_to_home_page()

    @pytest.mark.test3
    def test_verify_number_of_products(self):
        all_products = self.homepage.get_all_products()
        logger.info(f"Found: {len(all_products)} products")
        assert len(all_products) == 16, f"Expected total products: 17, Actual: {len(all_products)}"

        # first_product = all_products[0]
        # first_product.click()
        # logger.info(f"Clicked on first product")