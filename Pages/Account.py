import time

from Pages.BasePage import BasePage


class Account(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def Dactive_Account(self):
        self.click_element(BasePage.Setting)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.Click_Account)
        self.click_element(BasePage.Deactivate_Account)
        time.sleep(2)

    def Active_Account(self):
        self.click_element(BasePage.Setting)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.Click_Account)
        self.click_element(BasePage.Activate_Account)
        time.sleep(1)
