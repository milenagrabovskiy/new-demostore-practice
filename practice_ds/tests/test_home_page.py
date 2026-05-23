
import logging

import pytest

logger = logging.getLogger(__name__)

class TestHomePage:

    @pytest.mark.test3
    def test_verify_number_of_products(self):
        all_products = self.homepage.get_all_products()
        logger.info(f"Found: {len(all_products)} products")

        # first_product = all_products[0]
        # first_product.click()
        # logger.info(f"Clicked on first product")