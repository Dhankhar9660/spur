""" Test Page for Login Checks"""
import os
import time
import pyperclip
import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.RegistryPage import RegistryPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


class TestRegistry(BaseTest):
    # create method for Login and create object of Test_Login to access various functions from Parent Class
    EXP_title = (By.XPATH, "//div[@class='nexExp_heading']")
    body = (By.XPATH, "//div[@class='product-name']//h2")
    EXPERIENCE = "(//div[@class='product-name']//h2)[2]"

    @pytest.mark.alltest
    @pytest.mark.regression
    @pytest.mark.registry
    def test_add_to_registry(self, request):
        self.registry = LoginPage(self.driver)
        self.registry.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        self.registry = RegistryPage(self.driver)
        self.registry.registry()
        time.sleep(3)
        # title = self.registry.get_element_text(self.EXP_title)
        # print(title+" Added to registry")
        self.registry.click_element(BasePage.ADD_TO_REGISTRY)
        time.sleep(4)
        self.registry.click_on_hidden_element(self.EXPERIENCE)
        remove = self.registry.get_element_text(BasePage.ADD_TO_REGISTRY)
        try:
            assert remove == "REMOVE FROM REGISTRY"
            self.registry.click_element(BasePage.ADD_TO_REGISTRY)
            time.sleep(3)

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
            self.registry.refresh_page(self.driver)
            time.sleep(3)
            self.registry.click_element(BasePage.Log_Out)
            time.sleep(3)
            raise
        self.registry.click_element(BasePage.Log_Out)
        time.sleep(2)

    @pytest.mark.alltest
    @pytest.mark.regression
    @pytest.mark.addbucket
    def test_add_to_bucket_list(self, request):
        self.regist = LoginPage(self.driver)
        self.regist.login(BasePage.INDIVIDUAL_EMAIL, BasePage.AUTOMATION_PASSWORD)
        self.registry = RegistryPage(self.driver)
        self.registry.registry()
        time.sleep(3)
        # title = self.regist.get_element_text(self.EXP_title)
        # print(title+" Added to registry")
        self.regist.click_element(BasePage.ADD_TO_REGISTRY)
        time.sleep(3)
        self.regist.click_on_hidden_element(self.EXPERIENCE)
        remove = self.regist.get_element_text(BasePage.ADD_TO_REGISTRY)
        try:
            assert remove == "REMOVE FROM BUCKET LIST"
            print("test 2")
            self.regist.click_element(BasePage.ADD_TO_REGISTRY)

            # print(title + " " + Remove)
            time.sleep(3)

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
            self.registry.refresh_page(self.driver)
            time.sleep(3)
            self.registry.click_element(BasePage.Log_Out)
            time.sleep(3)
            raise
        self.registry.click_element(BasePage.Log_Out)
        time.sleep(2)

    @pytest.mark.alltest
    @pytest.mark.regression
    @pytest.mark.guestview
    def test_guest_view(self):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(4)

        self.regist = RegistryPage(self.driver)
        self.regist.Add_Registry(TestData.Exprience_Name, TestData.Exp_Actual_Name)
        self.regist.click_element(BasePage.View_Our_Url)
        time.sleep(1)
        self.regist.click_element(BasePage.Copy_Url)

        clipboard_text = pyperclip.paste()

        self.regist.click_element(BasePage.Close_Popup)

        self.regist.click_element(BasePage.Log_Out)
        time.sleep(3)
        self.regist.driver.get(clipboard_text)
        time.sleep(5)
        self.regist.driver.execute_script("window.scrollTo(0,700)")
        time.sleep(1)
        self.regist.send_keys(BasePage.Search_Product, TestData.Exprience_Name)
        time.sleep(5)
        self.regist.click_element(BasePage.Search)
        time.sleep(3)
        self.regist.driver.execute_script("window.scrollTo(0,1000)")
        self.regist.click_on_hidden_element(BasePage.Add_To_Cart)
        time.sleep(2)
        self.regist.driver.refresh()
        time.sleep(2)
        self.regist.click_element(BasePage.Click_On_Cart)
        try:
            product_name = self.regist.get_element_text(BasePage.Product)
            name_upper = TestData.Exprience_Name.upper()
            assert product_name == name_upper
            self.regist.click_element(BasePage.Remove_From_Cart)
            self.regist.click_element(BasePage.Click_Yes_Button)
        except AssertionError:
            print('Product not added.')
            raise
        time.sleep(2)

        # ---------------- Remove from registry _____________
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(3)
        self.remove_registry = RegistryPage(self.driver)
        self.remove_registry.Remove_From_Registry(TestData.Exprience_Name, TestData.Exp_Actual_Name)
        time.sleep(2)
        self.remove_registry.click_element(BasePage.Log_Out)
        time.sleep(2)
