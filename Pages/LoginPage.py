import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    def login(self, email, password):
        self.click_element(BasePage.LOGIN_ICON)
        self.clear_text_box(self.EMAIL)
        self.send_keys(self.EMAIL, email)
        self.clear_text_box(self.PASSWORD)
        self.send_keys(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)

