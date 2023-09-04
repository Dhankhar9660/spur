import time
import os
import pytest

from Pages.BasePage import BasePage
from Pages.ChangePassword import ChangePassword
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Config.config import TestData


class Test_change_password(BaseTest):

    @pytest.mark.changepassword
    @pytest.mark.alltest
    # ---test change password functionality without enter any information------
    def test_change_password_a(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("", "", "")
        try:
            old_pas_validation = self.login.get_element_text(BasePage.Old_Pas_Validation_1)
            assert old_pas_validation == 'Old Password is required'

            new_pas_validation = self.login.get_element_text(BasePage.New_Pas_Validation_1)
            assert new_pas_validation == 'New Password is required'

            confirm_pas_validation = self.login.get_element_text(BasePage.Confirm_Pas_Validation_1)
            assert confirm_pas_validation == 'Confirm Password is required'

        except AssertionError:
            print('password validation message is incorrect')
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
        self.login.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    # -----test change password functionality without enter old password---------
    def test_change_password_b(self, request):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("", "System@321", "System@321")
        try:
            old_pas_validation = self.login.get_element_text(BasePage.Old_Pas_Validation_1)
            assert old_pas_validation == 'Old Password is required'
        except AssertionError:
            print('validation of the old password input field is incorrect')
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
        self.login.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_c(self,
                               request):  # test change password functionality with enter incorrect password into old password
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("Admin@123", "System@321", "System@321")
        try:
            old_pas_validation = self.login.get_element_text(BasePage.Old_Pas_Validation_2)
            assert old_pas_validation == 'Your old password is incorrect'
        except AssertionError:
            print('validation of the old password  is incorrect')
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
        self.login.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    # test change password functionality with enter diffrent password into new password and confirm password
    def test_change_password_d(self, request):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("System@123", "System@321", "Admin@123")
        try:
            confirm_pas_validation = self.login.get_element_text(BasePage.Confirm_Pas_Validation_2)
            assert confirm_pas_validation == 'password and confirm password must match.'
        except AssertionError:
            print('validation does not match')
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
        self.login.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    # ----------------------------------test password combination------------------------------
    def test_change_password_e(self, request):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("System@123", 123, 123)
        time.sleep(3)
        try:
            new_pas_validation = self.login.get_element_text(BasePage.New_Pas_Validation_2)
            assert new_pas_validation == 'New Password length should be minimum 6.'

            confirm_pas_validation = self.login.get_element_text(BasePage.Confirm_Pas_Validation_3)
            assert confirm_pas_validation == 'Confirm Password length should be minimum 6.'

        except TimeoutError:
            print('validation is incorrect')
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
        self.login.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    @pytest.mark.regression
    # ----------test change password functionality with valid information----------------
    def test_change_password_f(self, request):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.login = ChangePassword(self.driver)
        self.login.Change_Password("123123", "System@321", "System@321")
        time.sleep(3)
        self.login.click_element(BasePage.Log_Out)
        try:
            self.login = LoginPage(self.driver)
            self.login.login(BasePage.COUPLE_EMAIL, "System@321")
            time.sleep(5)
            current_url = self.login.get_current_url()

            assert current_url == TestData.Profile_Url

        except AssertionError:
            print('User not able to login with new password')
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
        # ---- reset to old password----------
        self.login = ChangePassword(self.driver)
        self.login.Change_Password("System@321", "123123", "123123")
        time.sleep(1)
        self.login.click_element(BasePage.Log_Out)
