import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class OrderPage(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def order(self):
        # self.click_element(BasePage.DASHBOARD)
        time.sleep(3)
        # self.click_element(BasePage.ADD_TO_CART)
        self.click_element(BasePage.CHECKOUT)
        time.sleep(3)
        self.click_element(BasePage.BUYFORME)
        self.click_element(BasePage.NEXT)
        time.sleep(3)
        self.send_keys(BasePage.CCINPUT, BasePage.CC_Number)
        self.send_keys(BasePage.MONTH, BasePage.Month)
        self.send_keys(BasePage.YEAR, BasePage.Year)
        self.send_keys(BasePage.CVV, BasePage.cvv)
        self.click_element(BasePage.PLACE_ORDER)
        time.sleep(3)
