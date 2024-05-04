""" Test Page for Add new experience Checks"""
import os
import time
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.CreateEXP import CreateExp
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class TestCreateExp(BaseTest):
    # create method for experience and create object of Test_Add experience to access various function from Parent Class
    @pytest.mark.createxp
    @pytest.mark.alltest
    def test_create_exp(self, request):

        self.regist = LoginPage(self.driver)
        self.regist.login(BasePage.EP_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        self.exp = CreateExp(self.driver)
        self.exp.createexp()
        time.sleep(2)
        ourexp = self.exp.get_element_text(BasePage.EXP_HEADING)
        congmsg = self.exp.get_element_text(BasePage.EXP_cong_msg)

        try:
            assert ourexp == "CONGRATULATIONS!"
            assert congmsg == "Your experience has been successfully created. The Spur Experiences team will review " \
                              "and publish once approved."
            self.exp.click_on_hidden_element(BasePage.SUBMIT)
            time.sleep(4)
        except AssertionError:
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

        try:
            self.exp.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            self.exp.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            exp_list = (By.XPATH, "//div[@class='product-name']//h2")
            all_experiences = self.exp.get_list_of_elements(exp_list)
            name_all_exp = []
            for i in all_experiences:
                name_all_exp.append(i.text)
            assert self.exp.exp_name.upper() in name_all_exp
            print("your experience {" + self.exp.exp_name.upper() + "} has been created sucessfully")
        except AssertionError:
            print("experience is not created.")
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
