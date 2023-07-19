import time

import pytest

from Pages.BasePage import BasePage
from Pages.ChangePassword import ChangePassword
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Config.config import TestData


class Test_Change_Password(BaseTest):

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_a(self):  # test change password functionality without enter any information

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("", "", "")
        try:
            Old_Pas_Validation = self.asd.get_element_text(BasePage.Old_Pas_Validation_1)
            assert Old_Pas_Validation == 'Old Password is required'

            New_Pas_Validation = self.asd.get_element_text(BasePage.New_Pas_Validation_1)
            assert New_Pas_Validation == 'New Password is required'

            Confirm_Pas_Validation = self.asd.get_element_text(BasePage.Confirm_Pas_Validation_1)
            assert Confirm_Pas_Validation == 'Confirm Password is required'

        except AssertionError:
            print('password validation is incorrect')
            raise
        self.asd.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_b(self):  # test change password functionality without enter old password
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("", "System@321", "System@321")
        try:
            Old_Pas_Validation = self.asd.get_element_text(BasePage.Old_Pas_Validation_1)
            assert Old_Pas_Validation == 'Old Password is required'
        except AssertionError:
            print('validation of the old password input field is incorrect')
            raise
        self.asd.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_c(
            self):  # test change password functionality with enter incorrect password into old password
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("Admin@123", "System@321", "System@321")
        try:
            Old_Pas_Validation = self.asd.get_element_text(BasePage.Old_Pas_Validation_2)
            assert Old_Pas_Validation == 'Your old password is incorrect'
        except AssertionError:
            print('validation of the old password  is incorrect')
            raise
        self.asd.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_d(
            self):  # test change password functionality with enter diffrent password into new password and confirm password
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("System@123", "System@321", "Admin@123")
        try:
            Confirm_Pas_Validation = self.asd.get_element_text(BasePage.Confirm_Pas_Validation_2)
            assert Confirm_Pas_Validation == 'password and confirm password must match.'
        except AssertionError:
            print('validation does not match')
            raise
        self.asd.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_e(self):  # test password combination
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.refresh_page(self.driver)
        self.asd.Change_Password("System@123", 123, 123)
        try:
            New_Pas_Validation = self.asd.get_element_text(BasePage.New_Pas_Validation_2)
            assert New_Pas_Validation == 'New Password length should be minimum 6.'
            Confirm_Pas_Validation = self.asd.get_element_text(BasePage.Confirm_Pas_Validation_3)
            assert Confirm_Pas_Validation == 'Confirm Password length should be minimum 6.'
        except TimeoutError:
            print('validation is incorrect')
            raise
        self.asd.click_element(BasePage.Log_Out)

    @pytest.mark.changepassword
    @pytest.mark.alltest
    def test_change_password_f(self):  # test change password functionality with valid information
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("System@123", "System@321", "System@321")
        time.sleep(1)
        self.asd.click_element(BasePage.Log_Out)
        try:
            self.login = LoginPage(self.driver)
            self.login.login(BasePage.COUPLE_EMAIL, "System@321")
            time.sleep(5)
            Current_Url = self.asd.get_current_url()

            assert Current_Url == TestData.Profile_Url

        except AssertionError:
            print('User not able to login with new password')
            raise
        # ---- reset to old password----------
        self.asd = ChangePassword(self.driver)
        self.asd.Change_Password("System@321", "System@123", "System@123")
        time.sleep(1)
        self.asd.click_element(BasePage.Log_Out)
