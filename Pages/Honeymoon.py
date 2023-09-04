import time

import datetime
from Pages.BasePage import BasePage
from datetime import datetime


class Update_Honeymoon(BasePage):
    now = datetime.now()
    todaydate = now.strftime("%d")
    today = todaydate.lstrip('0')
    Date = f"//tbody//span[text() = '{today}']"

    def __int__(self, driver):
        super().__init__(driver)

    def Honeymoon(self, location, mob, loding):
        self.click_element(BasePage.Setting)
        time.sleep(4)
        self.click_element(BasePage.Honeymoon)
        self.clear_text_box(BasePage.Honymoon_Location)
        self.send_keys(BasePage.Honymoon_Location, location)
        self.clear_text_box(BasePage.Mobile_Number)
        self.send_keys(BasePage.Mobile_Number, mob)
        self.click_element(BasePage.Trip_Start_Date)
        time.sleep(1)
        self.click_on_hidden_element(self.Date)
        self.click_element(BasePage.Trip_End_Date)
        time.sleep(1)
        self.click_on_hidden_element(self.Date)
        self.clear_text_box(BasePage.Hotel_Loding)
        self.send_keys(BasePage.Hotel_Loding, loding)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.Update)
