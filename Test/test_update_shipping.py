import time

import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.UpdateShipping import Shipping
from Test.test_Base import BaseTest


class TestUpdateShipping(BaseTest):

    @pytest.mark.shipping
    @pytest.mark.alltest
    def test_update_shipping(self):

        self.spur = LoginPage(self.driver)
        self.spur.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.spur = Shipping(self.driver)
        self.spur.UpdateShipping("Test", "user", "only for testing", "Aruba")

        try:
            firstname = self.spur.get_element_value(BasePage.FirstName)
            assert firstname == 'Test'

            lastname = self.spur.get_element_value(BasePage.LastName)
            assert lastname == 'user'

            address = self.spur.get_element_value(BasePage.Address)
            assert address == 'only for testing'

            country = self.spur.get_element_text(BasePage.Country)
            assert country == "Aruba"

        except AssertionError:
            print('shipping page not updating')
            raise
        time.sleep(1)
        self.spur.UpdateShipping("QATest", "lastname", "only for testing Address", "Aruba")
        time.sleep(4)
        self.spur.click_element(BasePage.Log_Out)
        time.sleep(2)
