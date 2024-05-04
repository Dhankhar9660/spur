import time

import pytest

from Pages.BasePage import BasePage
from Pages.InvitePartner import InvitePartner
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest


class TestInvitePartner(BaseTest):

    @pytest.mark.partner
    @pytest.mark.alltest
    def test_update_partner(self):

        self.spur = LoginPage(self.driver)
        self.spur.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.spur = InvitePartner(self.driver)
        self.spur.invite_partner('testsk@yopmail.com')
        time.sleep(2)
        try:
            self.spur.refresh_page(self.driver)
            email = self.spur.get_element_value(BasePage.Partner_Email)
            assert email == 'testsk@yopmail.com'
            # ------ reset to old partner's email -----------
            self.spur.invite_partner('partner1@yopmail.com')
            time.sleep(2)

        except AssertionError:
            print('Partner Email is not updating.')
            raise
        time.sleep(2)
        self.spur.click_element(BasePage.Log_Out)
        time.sleep(2)
