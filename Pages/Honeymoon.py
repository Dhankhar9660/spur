import time

import datetime
from Pages.BasePage import BasePage


class Update_Honeymoon(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def Honeymoon(self, location, mob, start_date, end_date, loding):
        self.click_element(BasePage.Setting)
        time.sleep(4)
        self.click_element(BasePage.Honeymoon)
        self.clear_text_box(BasePage.Honymoon_Location)
        self.send_keys(BasePage.Honymoon_Location, location)
        self.clear_text_box(BasePage.Mobile_Number)
        self.send_keys(BasePage.Mobile_Number, mob)
        self.click_element(BasePage.Trip_Start_Date)
        time.sleep(1)
        self.click(BasePage.Date)
        self.click_element(BasePage.Trip_End_Date)
        time.sleep(1)
        self.click(BasePage.Date)
        self.clear_text_box(BasePage.Hotel_Loding)
        self.send_keys(BasePage.Hotel_Loding, loding)

        self.click(BasePage.Update)
