import os
import time
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class TestClaimVoucher(BaseTest):
    # ______________create method for claim voucher and create all test cases____________________
    setting = (By.XPATH, "//a[text()='Settings']")
    claim_voucher = "(//a[text()='CLAIM VOUCHER'])[1]"
    claim_input = (By.XPATH, "//input[@id='redeem_coupon_188']")
    claim_button = (By.XPATH, "//input[@name='redeem_submit_188']")
    invalid_message = (By.XPATH, "//div[@class='help-block ng-star-inserted']")

    @pytest.mark.claim
    @pytest.mark.alltest
    def test_claim_voucher_login(self, request):

        self.claim = LoginPage(self.driver)
        self.claim.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        self.claim.click_element(self.setting)
        time.sleep(4)
        self.claim.click_on_hidden_element(self.claim_voucher)
        time.sleep(2)
        self.claim.send_keys(self.claim_input, "832682200094292731001")
        self.claim.click_element(self.claim_button)

        message = ""
        try:
            message = self.claim.get_element_text(self.invalid_message)
        except TimeoutError:
            print("Error message not showing.")
            self.claim.click_element(BasePage.LOGOUT)
            raise

        try:
            assert message == "This voucher number is not valid. Please contact info@spurexperiences.com for " \
                              "assistance."
            self.claim.click_element(BasePage.LOGOUT)
        except AssertionError:
            print(message + "This message not correct")
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
