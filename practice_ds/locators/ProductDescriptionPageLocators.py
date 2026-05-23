from selenium.webdriver.common.by import By


class ProductDescriptionPageLocators:

    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="product-31"]/div[2]/form/button')
    # ADD_TO_CART_BTN = (By.CLASS_NAME, "single_add_to_cart_button")
    # ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.single_add_to_cart_button")
    CART_BTN = (By.ID, "site-header-cart")
