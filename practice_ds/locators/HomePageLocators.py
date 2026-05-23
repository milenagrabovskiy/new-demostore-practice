from selenium.webdriver.common.by import By


class HomePageLocators:

    ALL_PRODUCTS = (By.CSS_SELECTOR, "li.product")
    CART_BTN = (By.ID, "site-header-cart")