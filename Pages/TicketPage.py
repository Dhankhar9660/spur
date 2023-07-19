import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class TicketPage(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def ticket(self):
        self.click_element(BasePage.TICKET)
        time.sleep(2)
        self.click_element(BasePage.TKTTYPE)
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 600)")
        self.send_keys(BasePage.ticketnameinput, BasePage.ticket)
        self.click_element(BasePage.search_button)

        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(5)
        self.click_element(BasePage.EVENT)
        time.sleep(5)
        self.click_element(BasePage.TICKETBUY)
        time.sleep(2)
        self.click_element(BasePage.SELECTACCOUNT)
        self.click_element(BasePage.BUYFORME)
        self.click_element(BasePage.NEXT1)
        time.sleep(3)
        self.send_keys(BasePage.CCINPUT, BasePage.CC_Number)
        self.send_keys(BasePage.MONTH, BasePage.Month)
        self.send_keys(BasePage.YEAR, BasePage.Year)
        self.send_keys(BasePage.CVV, BasePage.cvv)
        self.click_element(BasePage.PLACE_ORDER)
        time.sleep(3)
