import time

from Pages.BasePage import BasePage


class ChangePassword(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def Change_Password(self, old_pas, new_pas, confirm_pas):
        self.click_element(BasePage.Setting)
        time.sleep(3)
        self.click(BasePage.Click_ChangePassword)
        self.clear_text_box(BasePage.Old_Password)
        self.send_keys(BasePage.Old_Password, old_pas)
        self.clear_text_box(BasePage.New_Password)
        self.send_keys(BasePage.New_Password, new_pas)
        self.clear_text_box(BasePage.Confirm_Password)
        self.send_keys(BasePage.Confirm_Password, confirm_pas)
        self.click_element(BasePage.Submit)
        time.sleep(1)
