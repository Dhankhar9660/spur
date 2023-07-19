import time

import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.UpdateShipping import Shipping
from Test.test_Base import BaseTest


class Test_Update_Shipping(BaseTest):

    @pytest.mark.shipping
    @pytest.mark.alltest
    def test_update_shipping(self):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = Shipping(self.driver)
        self.asd.UpdateShipping("Anil", "Kumar", "only for testing", "Johan")

        try:
            FirstName = self.asd.get_element_value(BasePage.FirstName)
            assert FirstName == 'Anil'

            LastName = self.asd.get_element_value(BasePage.LastName)
            assert LastName == 'Kumar'

            Address = self.asd.get_element_value(BasePage.Address)
            assert Address == 'only for testing'

            Country = self.asd.get_element_text(BasePage.Country)
            assert Country == 'Johannesburg'

        except AssertionError:
            print('shipping page not updating')
            raise
        time.sleep(1)
        self.asd.click_element(BasePage.Log_Out)
