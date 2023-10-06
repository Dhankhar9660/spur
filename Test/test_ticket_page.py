""" Test Page for Login Checks"""
import os
import time
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.TicketsearchPage import TicketPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.alltesta
class Test_Ticket(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class

    def test_ticket_search(self, request):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        # time.sleep(5)
        self.ticket = TicketPage(self.driver)
        self.ticket.ticket_search()
        time.sleep(7)

        # try:
        #     assert "ORDERCON" == BasePage.Orderconf
        # except AssertionError:
        #     timestamp = str(int(time.time()))
        #
        #     # Get the current test name
        #     test_name = request.node.name
        #     # Create a unique file name using the test name and timestamp
        #     file_name = f"{test_name}_{timestamp}.png"
        #
        #     # Specify the directory path to save the screenshot
        #     directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"
        #
        #     # Create the full path by joining the directory path and file name
        #     screenshot_path = os.path.join(directory, file_name)
        #
        #     # Save the screenshot
        #     self.driver.save_screenshot(screenshot_path)
        #     raise
