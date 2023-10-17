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
    def ticket_search(self):
        self.click_element(BasePage.TICKET)
        time.sleep(2)
        self.click_element(BasePage.TKTTYPE)
        time.sleep(12)
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.send_keys(BasePage.ticketnameinput, BasePage.ticket)
        self.click_element(BasePage.search_button)
        time.sleep(8)
