from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
import time


class InvitePartner(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def invite_partner(self, email):
        self.click_element(BasePage.Setting)

        time.sleep(5)
        self.click_element(BasePage.Invite)

        # revoke_email = (By.XPATH, "//input[@value = 'REVOKE']")

        try:
            self.driver.find_element(By.XPATH, "//input[@value = 'REVOKE']").click()
            time.sleep(4)
            self.click_element(BasePage.Invite)
        except NoSuchElementException:
            pass

        self.send_keys(BasePage.Email_Invitation, email)
        self.click_element(BasePage.Click_Invite)
