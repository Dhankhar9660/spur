""" Test Page for Login Checks
Author: Balkishan Dhankhar"""
import os
import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.CharityRegisterPage import CharityregPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup
class Test_EXPRegistration(BaseTest):
    Charityname = (By.XPATH, "//h1[@class='main_heading']")
    NAME = "WELCOME, " + CharityregPage.CHARITYNAME

    def test_EXPRegistration(self, request):

        self.chareg = CharityregPage(self.driver)
        self.chareg.charityregister()
        time.sleep(3)
        name = self.chareg.get_element_text(self.Charityname)
        try:
            assert name == self.NAME
        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/hp/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
