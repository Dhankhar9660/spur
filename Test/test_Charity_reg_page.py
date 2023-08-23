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


class Test_CHARITY_SIGNUP(BaseTest):
    Charityname = (By.XPATH, "//h1[@class='main_heading']")
    NAME = "WELCOME, " + CharityregPage.CHARITYNAME
    Close = (By.XPATH, "//span[@class='closeImg']")

    @pytest.mark.alltest
    @pytest.mark.regression
    @pytest.mark.signup
    def test_charity_signup(self, request):

        self.chareg = CharityregPage(self.driver)
        self.chareg.charityregister()
        time.sleep(3)
        name = self.chareg.get_element_text(self.Charityname)
        self.chareg.click_element(self.Close)
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
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

        try:
            menu = (By.XPATH, "//li[@class='active']//parent::ul//child::li")
            mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
            time.sleep(2)
            self.chareg.click_element(mydashboard)
            time.sleep(2)
            menuoption = self.chareg.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_charity, menulist))
            print("charity signup working fine.")
            self.chareg.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
            print("charity signup  not working.")
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
