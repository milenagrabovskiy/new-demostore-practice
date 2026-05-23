from selenium.webdriver.common.by import By


class CartPageLocators:
    ADD_COUPON_BTN = (By.CSS_SELECTOR, "button.wc-block-components-panel__button")
    COUPON_INPUT_FIELD = (By.ID, "wc-block-components-totals-coupon__input-0")
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button.wc-block-components-button.wc-block-components-totals-coupon__button')
    CART_TOTAL = (By.CSS_SELECTOR, "div.wc-block-components-totals-item__value")