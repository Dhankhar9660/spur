import time

import pytest

from Config.config import TestData
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from Pages.ChangePassword import ChangePassword
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Forgot_Password import Forgot_password

newemail = "projectonqa@gmail.com"
apppassword = "reqfailndcijwifo"
subject = "Forgot Password"
imap_server = "imap.gmail.com"
NewPassword = "System@1234"


class Test_forgot_password(BaseTest):
    @pytest.mark.forgotpassword
    @pytest.mark.regression
    @pytest.mark.alltest
    def test_forgot_password(self, request):
        # ----------reset password-----------
        self.forgot = Forgot_password(self.driver)
        self.forgot.forgot_password(newemail, apppassword, NewPassword)
        time.sleep(7)

        try:
            # --------login with new password--------------
            self.forgot = LoginPage(self.driver)
            self.forgot.login(newemail, NewPassword)
            time.sleep(5)
            url = self.forgot.get_current_url()
            assert url == TestData.Profile_Url

            # ---------- password change to old password--------
            self.forgot = ChangePassword(self.driver)
            self.forgot.Change_Password(NewPassword, "123123", "123123")
            time.sleep(2)

        except AssertionError:
            print('Forgot password not working.')
            raise

        self.forgot.click_element(BasePage.Log_Out)
        time.sleep(2)
