import time

import pytest

from Pages.BasePage import BasePage

from Pages.Honeymoon import Update_Honeymoon
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest


class Test_Honeymoon(BaseTest):

    @pytest.mark.honeymoon
    @pytest.mark.alltest
    def test_update_honeymoon(self):
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.asd = Update_Honeymoon(self.driver)
        self.asd.Honeymoon("New Jersey, USA", 7890098765, "July 12, 2023", "July 24, 2023", "Testing")
        time.sleep(1)
        try:
            Location = self.asd.get_element_value(BasePage.Honymoon_Location)
            assert Location == "New Jersey, USA"

            Mob_Number = self.asd.get_element_value(BasePage.Mobile_Number)
            assert Mob_Number == '7890098765'

            Trip_Start_Date = self.asd.get_element_value(BasePage.Trip_Start_Date)
            assert Trip_Start_Date == "July 24, 2023"

            Trip_End_Date = self.asd.get_element_value(BasePage.Trip_End_Date)
            assert Trip_End_Date == "July 24, 2023"

            Hotel_Loding = self.asd.get_element_value(BasePage.Hotel_Loding)
            assert Hotel_Loding == "Testing"

        except Exception:
            print("Honeymoon not updating")
            raise
        self.asd.click_element(BasePage.Log_Out)
