""" Test Page for Add new experience Checks"""
import os
import time
import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.CreateEXP import CreateExp
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class Test_Create_Exp(BaseTest):
    # create method for experience and create object of Test_Add experience to access various function from Parent Class
    @pytest.mark.createxp
    def test_create_exp(self, request):

        self.regist = LoginPage(self.driver)
        self.regist.login(BasePage.EP_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        self.exp = CreateExp(self.driver)
        self.exp.Createexp()
        time.sleep(2)

        OUREXP = self.exp.get_element_text(BasePage.EXP_HEADING)
        try:
            assert OUREXP == "WELCOME, TEST"
            self.exp.click_element(BasePage.SUBMIT)

        except AssertionError:
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
