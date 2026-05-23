import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions



@pytest.fixture(scope="class")
def init_driver(request):
    browser = os.getenv("BROWSER", "chrome")
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()