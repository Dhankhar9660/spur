import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Exp_search_by_location(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def exp_by_location(self):
        self.click_element(BasePage.TICKET)
