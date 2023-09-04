import time
import pyperclip
import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest


class Test_URL(BaseTest):

    @pytest.mark.copyurl
    @pytest.mark.alltest
    def test_registryurl(self):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        self.asd = BasePage(self.driver)
        self.asd.click_element(BasePage.View_Our_Url)
        time.sleep(1)
        self.asd.click_element(BasePage.Copy_Url)

        clipboard_text = pyperclip.paste()
        try:
            assert clipboard_text == TestData.Registry_Url
        except AssertionError:
            print('Url not found')
            raise

        self.asd.click_element(BasePage.Close_Popup)
        time.sleep(2)
        self.asd.click_element(BasePage.Log_Out)

        # Print the clipboard text
        # print("Clipboard text:", clipboard_text)
