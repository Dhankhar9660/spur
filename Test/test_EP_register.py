""" Test Page for Login Checks
Author: Balkishan Dhankhar"""
import os
import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.ExpProviderPageReg import ExpproPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class Test_EXPRegistration(BaseTest):
    Head1 = (By.XPATH, "//h1[@class='main_heading']")
    Close = (By.XPATH, "//span[@class='closeImg']")

    @pytest.mark.signup
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_ep_rgistration(self, request):

        self.expreg = ExpproPage(self.driver)
        self.expreg.expregister()
        time.sleep(5)
        head = self.expreg.get_element_text(self.Head1)
        heading = "STEP TWO- PAYMENT INFO"
        # print(head)
        try:
            assert head == heading
            self.expreg.click_element(self.Close)
            time.sleep(5)
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
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
            self.expreg.click_element(mydashboard)
            time.sleep(2)
            menuoption = self.expreg.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_ep, menulist))
            print("EP signup working fine.")
            self.expreg.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
            print("EP signup  not working.")
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
