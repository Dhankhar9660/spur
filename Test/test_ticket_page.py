""" Test Page for Login Checks"""

import time
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.TicketsearchPage import TicketPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class TestTicket(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class
    @pytest.mark.ticketsearch
    @pytest.mark.regression
    @pytest.mark.alltesta
    def test_ticket_search(self):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        # time.sleep(5)
        self.ticket = TicketPage(self.driver)
        self.ticket.ticket_search()
        time.sleep(2)
        search_list = (By.XPATH, "//div[@class='eventInfo']")
        try:
            ticketnumber = len(self.ticket.get_list_of_elements(search_list))
            print(ticketnumber)
            if ticketnumber > 0:
                print("List is not empty!")
            else:
                raise ValueError("List is empty!")

        except ValueError as e:
            print(e)
