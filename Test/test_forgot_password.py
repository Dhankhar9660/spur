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
    @pytest.mark.alltest
    def test_forgot_password(self, request):
        # ----------reset password-----------
        self.forgot = Forgot_password(self.driver)
        self.forgot.forgot_password(newemail, apppassword, NewPassword)
        time.sleep(7)

        try:
            # --------login with new password--------------
            self.login = LoginPage(self.driver)
            self.login.login(newemail, NewPassword)
            time.sleep(5)
            url = self.login.get_current_url()
            assert url == TestData.Profile_Url
            # ---------- password change to old password--------
            self.asd = ChangePassword(self.driver)
            self.asd.Change_Password(NewPassword, "System@123", "System@123")
            time.sleep(1)
            self.asd.click_element(BasePage.Log_Out)
        except AssertionError:
            print('password not changed')
            raise

        self.asd.click_element(BasePage.Log_Out)
