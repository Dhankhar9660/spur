import time

import pytest

from Pages.Account import Account
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest


class Test_Account(BaseTest):

    @pytest.mark.account
    @pytest.mark.alltest
    def test_deactivate_account(self):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.account = Account(self.driver)
        self.account.Dactive_Account()
        Text = self.account.get_element_text(BasePage.AccountInactive)
        print(Text)
        try:
            assert Text == BasePage.AccountInactiveMsg
        except AssertionError:
            self.account.click_element(BasePage.Log_Out)
            raise

        self.account.Active_Account()
        time.sleep(3)
        self.account.click_element(BasePage.Log_Out)
