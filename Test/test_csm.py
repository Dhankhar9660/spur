import os
import time
import sys
import pytest

from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Cms import CmsPage

import openpyxl
from datetime import datetime


class Test_Login(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class and check all login test cases
    @pytest.mark.smoke
    def test_about(self, request):

        self.asd = CmsPage(self.driver)
        self.asd.about()
        time.sleep(8)
        Page_title = self.asd.get_element_text(BasePage.ABOUT_HEADING)

        try:
            assert Page_title == "About Spur"

        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    def test_howitwork(self, request):

        self.asd = CmsPage(self.driver)
        self.asd.howitwork()
        time.sleep(8)
        Page_title = self.asd.get_element_text(BasePage.ABOUT_HEADING)

        try:
            assert Page_title == "How It Works"

        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
