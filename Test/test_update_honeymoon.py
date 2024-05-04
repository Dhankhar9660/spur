import time
import os
import pytest
from Pages.BasePage import BasePage
from Pages.Honeymoon import Update_Honeymoon
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
import datetime


class TestHoneymoon(BaseTest):
    today = datetime.datetime.now().strftime("%B %d, %Y")

    @pytest.mark.honeymoon
    @pytest.mark.alltest
    def test_update_honeymoon(self, request):
        self.honeymoon = LoginPage(self.driver)
        self.honeymoon.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.honeymoon = Update_Honeymoon(self.driver)
        self.honeymoon.Honeymoon("New Jersey, USA", 8787878787, "Testing")
        time.sleep(4)
        try:
            location = self.honeymoon.get_element_value(BasePage.Honymoon_Location)
            assert location == "New Jersey, USA"

            mob_number = self.honeymoon.get_element_value(BasePage.Mobile_Number)
            assert mob_number == '8787878787'

            trip_start_date = self.honeymoon.get_element_value(BasePage.Trip_Start_Date)
            assert trip_start_date == self.today

            trip_end_date = self.honeymoon.get_element_value(BasePage.Trip_End_Date)
            assert trip_end_date == self.today

            hotel_landing = self.honeymoon.get_element_value(BasePage.Hotel_Loding)
            assert hotel_landing == "Testing"

        except Exception:
            print("Honeymoon not updating")
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
        self.honeymoon.Honeymoon("New York, NY, USA", 9898989898, "Testing hotel")
        time.sleep(5)
        self.honeymoon.click_element(BasePage.Log_Out)
        time.sleep(2)
