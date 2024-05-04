import re
import time
import os
import pytest
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class TestPriceFilter(BaseTest):
    remove_filter = (By.XPATH, "//a//i[@class = 'fa fa-times']")

    # --------------------------------------50 <= item <= 100-----------------------------------------------------
    @pytest.mark.pricefilter
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_price_filter_a(self, request):

        login = LoginPage(self.driver)
        login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        login.click_element(BasePage.ADDEXP)
        time.sleep(8)
        filter_option = (By.XPATH, "(//ul[@class = 'filter_typeoption']//li)[3]")
        login.click_element(filter_option)
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        allpricelist = (By.XPATH, "//div[starts-with(text(), ' $')]")

        all_price = login.get_list_of_elements(allpricelist)
        pricelist = []
        for i in all_price:
            pricelist.append(i.text)

        def extract_numeric_value(s):
            match = re.search(r'\d+', s)

            if match:
                return int(match.group())
            return None

        allproductprice = [extract_numeric_value(item) for item in pricelist]

        try:
            assert all(50 <= item <= 100 for item in allproductprice)

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

            # ----------------------------Save the screenshot----------------------------------
            self.driver.save_screenshot(screenshot_path)
            raise

        login.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        # login.click_element(self.remove_filter)
        # time.sleep(3)

        login.click_element(BasePage.Log_Out)
        time.sleep(2)

    # ------------------------------------100 <= item <= 200-----------------------------------------
    @pytest.mark.pricefilter
    @pytest.mark.alltest
    def test_price_filter_b(self, request):
        login = LoginPage(self.driver)
        login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        login.click_element(BasePage.ADDEXP)
        time.sleep(8)
        ab = (By.XPATH, "(//ul[@class = 'filter_typeoption']//li)[4]")
        login.click_element(ab)
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        itemlist = (By.XPATH, "//div[starts-with(text(), ' $')]")
        all_price = login.get_list_of_elements(itemlist)
        pricelist = []
        for i in all_price:
            pricelist.append(i.text)

        def extract_numeric_value(s):
            match = re.search(r'\d+', s)

            if match:
                return int(match.group())
            return None

        allproductprice = [extract_numeric_value(item) for item in pricelist]
        print(allproductprice)
        try:
            assert all(100 <= item <= 200 for item in allproductprice)

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

        login.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        login.click_element(self.remove_filter)
        time.sleep(3)

        login.click_element(BasePage.Log_Out)

    # -----------------------------------200 <= item ----------------------------------
    @pytest.mark.pricefilter
    @pytest.mark.alltest
    def test_price_filter_c(self, request):
        login = LoginPage(self.driver)
        login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        login.click_element(BasePage.ADDEXP)
        time.sleep(8)
        ab = (By.XPATH, "(//ul[@class = 'filter_typeoption']//li)[5]")
        login.click_element(ab)
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        itemlist = (By.XPATH, "//div[starts-with(text(), ' $')]")
        all_price = login.get_list_of_elements(itemlist)
        pricelist = []
        for i in all_price:
            pricelist.append(i.text)

        def extract_numeric_value(s):
            match = re.search(r'\d+', s)

            if match:
                return int(match.group())
            return None

        allproductprice = [extract_numeric_value(item) for item in pricelist]
        print(allproductprice)
        try:
            assert all(item >= 200 for item in allproductprice)

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

        login.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        login.click_element(self.remove_filter)
        time.sleep(3)

        login.click_element(BasePage.Log_Out)

    # -----------------------------------0 <= item <= 50--------------------------------------
    @pytest.mark.pricefilter
    @pytest.mark.alltest
    def test_price_filter_d(self, request):

        login = LoginPage(self.driver)
        login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        login.click_element(BasePage.ADDEXP)
        time.sleep(8)
        ab = (By.XPATH, "(//ul[@class = 'filter_typeoption']//li)[2]")
        login.click_element(ab)
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        itemlist = (By.XPATH, "//div[starts-with(text(), ' $')]")

        all_price = login.get_list_of_elements(itemlist)
        pricelist = []
        for i in all_price:
            pricelist.append(i.text)

        # a = login.extract_numeric_value()

        def extract_numeric_value(s):
            match = re.search(r'\d+', s)

            if match:
                return int(match.group())
            return None

        allproductprice = [extract_numeric_value(item) for item in pricelist]
        print(allproductprice)

        try:
            assert all(0 <= item <= 50 for item in allproductprice)

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

        login.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        login.click_element(self.remove_filter)
        time.sleep(3)

        login.click_element(BasePage.Log_Out)
