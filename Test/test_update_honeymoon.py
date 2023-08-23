import time

import pytest

from Pages.BasePage import BasePage

from Pages.Honeymoon import Update_Honeymoon
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
import datetime

class Test_Honeymoon(BaseTest):
    today = datetime.datetime.now().strftime("%B %d, %Y")

    @pytest.mark.honeymoon
    @pytest.mark.alltest
    def test_update_honeymoon(self):
        self.honeymoon = LoginPage(self.driver)
        self.honeymoon.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.honeymoon = Update_Honeymoon(self.driver)
        self.honeymoon.Honeymoon("New Jersey, USA", 8787878787, "Testing")
        time.sleep(4)
        try:
            Location = self.honeymoon.get_element_value(BasePage.Honymoon_Location)
            assert Location == "New Jersey, USA"

            Mob_Number = self.honeymoon.get_element_value(BasePage.Mobile_Number)
            assert Mob_Number == '8787878787'

            Trip_Start_Date = self.honeymoon.get_element_value(BasePage.Trip_Start_Date)
            assert Trip_Start_Date == self.today

            Trip_End_Date = self.honeymoon.get_element_value(BasePage.Trip_End_Date)
            assert Trip_End_Date == self.today

            Hotel_Loding = self.honeymoon.get_element_value(BasePage.Hotel_Loding)
            assert Hotel_Loding == "Testing"

        except Exception:
            print("Honeymoon not updating")
            raise
        self.honeymoon.Honeymoon("New York, NY, USA", 9898989898, "Testing hotel")
        time.sleep(5)
        self.honeymoon.click_element(BasePage.Log_Out)
        time.sleep(2)
