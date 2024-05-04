""" Test Page for friend request Checks"""
import os
import time
import pytest
from Pages.LoginPage import LoginPage
from Pages.Booking import Booking
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.booking
class TestBooking(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class

    def test_booking(self, request):
        try:
            self.regist = LoginPage(self.driver)
            self.regist.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
            time.sleep(10)
            self.booking = Booking(self.driver)
            self.booking.booknow()
            time.sleep(3)
        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshotp
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
