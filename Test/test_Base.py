import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("init_driver_here")
class BaseTest:
    driver: WebDriver
    pass
