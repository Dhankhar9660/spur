import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage


class CmsPage(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    def about(self):
        self.hover_element(BasePage.ABOUTUS)
        self.click_element(BasePage.ABOUT_SPUR)

    def howitwork(self):
        self.hover_element(BasePage.ABOUTUS)
        self.click_element(BasePage.HOWITWORK)
