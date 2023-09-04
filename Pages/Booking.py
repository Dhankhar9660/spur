import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Booking(BasePage):

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page action

    def Add_to_cart(self, expname):
        # self.click_element(BasePage.DASHBOARD)
        self.click_element(BasePage.HOME)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.send_keys(BasePage.SEARCHBOXEXP, expname)
        time.sleep(3)
        self.click_element(BasePage.SEARCHITEM)
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 950)")
        time.sleep(3)
        self.click_element(BasePage.Buy_AS_VOUCHER)

    def booknow(self):
        # self.click_element(BasePage.DASHBOARD)
        self.click_element(BasePage.HOME)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.send_keys(BasePage.SEARCHBOXEXP, BasePage.REZDYEXP)
        time.sleep(3)
        self.click_element(BasePage.SEARCHITEM)
        # self.click_element(BasePage.QTY)
        self.send_keys(BasePage.QTY, "2 People")
        self.click_element(BasePage.CALENDER)
        self.click_element(BasePage.DATE)
        self.click_element(BasePage.TIMESLOT)
