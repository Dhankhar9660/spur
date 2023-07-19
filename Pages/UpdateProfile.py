import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class UpdateProfile(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def Update_Profile(self, Fname, Lname, Phone, PFname, PLname, Email, Date, Greet, Hastag, Region):
        self.click_element(BasePage.Setting)
        time.sleep(3)
        self.clear_text_box(BasePage.First_Name)
        self.send_keys(BasePage.First_Name, Fname)
        self.clear_text_box(BasePage.Last_Name)
        self.send_keys(BasePage.Last_Name, Lname)
        self.clear_text_box(BasePage.Phone_Number)
        self.send_keys(BasePage.Phone_Number, Phone)
        self.clear_text_box(BasePage.Partner_First_Name)
        self.send_keys(BasePage.Partner_First_Name, PFname)
        self.clear_text_box(BasePage.Partner_Last_Name)
        self.send_keys(BasePage.Partner_Last_Name, PLname)
        self.clear_text_box(BasePage.Partner_Email)
        self.send_keys(BasePage.Partner_Email, Email)
        self.clear_text_box(BasePage.Wedding_Date)
        self.send_keys(BasePage.Wedding_Date, Date)
        self.clear_text_box(BasePage.Greetings)
        self.send_keys(BasePage.Greetings, Greet)
        self.clear_text_box(BasePage.Couple_Hashtag)
        self.send_keys(BasePage.Couple_Hashtag, Hastag)
        self.clear_text_box(BasePage.Home_Region)
        self.send_keys(BasePage.Home_Region, Region)
        time.sleep(2)
