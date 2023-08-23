import time

import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.UpdateProfile import UpdateProfile
from Test.test_Base import BaseTest


class Test_Update_Profile(BaseTest):

    @pytest.mark.profile
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_update_profile(self):
        self.update = LoginPage(self.driver)
        self.update.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)

        self.update = UpdateProfile(self.driver)
        self.update.Update_Profile("QAtest", "user", 9876543210, "newpartner", "test", "partner11@yopmail.com",
                                   "Thanks for the visiting", "Hss", "New Jersey")
        self.update.refresh_page(self.update.driver)
        time.sleep(5)
        try:
            first_name = self.update.get_element_value(BasePage.First_Name)
            assert first_name == "QAtest"

        except AssertionError:
            print("first name is not updating")
            raise

        try:
            last_name = self.update.get_element_value(BasePage.Last_Name)
            assert last_name == "user"

        except AssertionError:
            print("last name is not updating")
            raise

        try:
            phone_number = self.update.get_element_value(BasePage.Phone_Number)
            assert phone_number == "98765 43210"

        except AssertionError:
            print("phone number is not updating")
            raise

        try:
            partner_first_name = self.update.get_element_value(BasePage.Partner_First_Name)
            assert partner_first_name == "newpartner"

        except AssertionError:
            print("partner_first_name is not updating")
            raise

        try:
            Partner_Last_Name = self.update.get_element_value(BasePage.Partner_Last_Name)
            assert Partner_Last_Name == "test"

        except AssertionError:
            print("Partner_Last_Name is not updating")
            raise

        try:
            Partner_Email = self.update.get_element_value(BasePage.Partner_Email)
            assert Partner_Email == "partner11@yopmail.com"

        except AssertionError:
            print("Partner_Email is not updating")
            raise

        # try:
        #     Wedding_Date = self.asd.get_element_value(BasePage.Wedding_Date)
        #     assert Wedding_Date == "July 6, 2023"
        #
        # except AssertionError:
        #     print("Wedding_Date is not updating")
        #     raise

        try:
            Greetings = self.update.get_element_value(BasePage.Greetings)
            assert Greetings == "Thanks for the visiting"

        except AssertionError:
            print("Greetings is not updating")
            raise

        try:
            Couple_Hashtag = self.update.get_element_value(BasePage.Couple_Hashtag)
            assert Couple_Hashtag == "Hss"

        except AssertionError:
            print("Couple_Hashtag is not updating")
            raise

        try:
            Home_Region = self.update.get_element_value(BasePage.Home_Region)
            assert Home_Region == "New Jersey"

        except AssertionError:
            print("Home_Region is not updating")
            raise
        # ------- reset to old data----------
        self.update.Update_Profile("Balkishan", "Dhankhar", 9999999999, "testpartner", "partner", "partner@yopmail.com",
                                   "test Thanks for the visiting", "Hass", "New Jersey")
        time.sleep(2)
        self.update.click_element(BasePage.Log_Out)
