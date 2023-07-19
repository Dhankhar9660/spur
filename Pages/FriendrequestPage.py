import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Friends(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def Friendreq(self):
        self.click_element(BasePage.FRIENDS)
        time.sleep(5)
        self.click_element(BasePage.FINDFRIENDS)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(5)
        self.click_element(BasePage.FRIENDREQUEST)
        time.sleep(3)
        self.click_element(BasePage.FRIENDS)
