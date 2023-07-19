import time

import pytest

from Pages.BasePage import BasePage
from Pages.InvitePartner import InvitePartner
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest


class Test_Invite_Partner(BaseTest):

    @pytest.mark.partner
    @pytest.mark.alltest
    def test_update_invite_partner(self):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = InvitePartner(self.driver)
        self.asd.invite_partner('testsk@yopmail.com')
        time.sleep(2)
        try:
            self.asd.refresh_page(self.driver)
            email = self.asd.get_element_value(BasePage.Partner_Email)
            assert email == 'testsk@yopmail.com'
            # ------ reset to old partner's email -----------
            self.asd.invite_partner('partner@yopmail.com')
            time.sleep(2)
        except AssertionError:
            print('Partner Email is not updating')
            raise
