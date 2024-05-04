""" Test Page for friend request Checks"""
import os
import time
import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.FriendrequestPage import Friends
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class Test_Friendreq(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class
    @pytest.mark.friendrequest
    @pytest.mark.alltest
    def test_Friendreq(self, request):
        self.regist = LoginPage(self.driver)
        self.regist.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(8)
        self.friend = Friends(self.driver)
        self.friend.Friendreq()
        time.sleep(3)
        reqcncl = self.friend.get_element_text(BasePage.FRIENDREQUESTCNSL)

        try:
            assert reqcncl == "Cancel Request"
            self.friend.click_element(BasePage.FRIENDREQUESTCNSL)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
