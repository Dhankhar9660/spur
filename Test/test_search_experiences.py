import os
import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Search_experiences import SearchExp


class TestCmsPage(BaseTest):
    policy = (By.XPATH, "//h2[@class='termsHeading']")
    results = (By.XPATH, "//div[@class='wsa_list_head']")
    heading = (By.XPATH, "//h2//a")

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.searchexp
    def test_search_on_homepage(self, request):

        self.search = SearchExp(self.driver)
        self.search.search_exp_by_name_on_home("Test live exp")
        time.sleep(8)

        try:
            searchlist = self.search.get_list_of_elements(self.heading)
            expname = []
            for i in searchlist:
                expname.append(i.text)
        except TimeoutException:
            print("search list is not loading")
            self.search.click_element(BasePage.HOME)
            raise

        try:
            assert "TEST LIVE EXP (NEW YORK)" in expname
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
        except AssertionError:
            # Create a unique timestamp for the screenshot
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
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.searchexp
    def test_search_by_name_and_location(self, request):

        self.search = SearchExp(self.driver)
        self.search.search_exp_by_name_and_location("Test live exp", "New york")
        time.sleep(8)

        try:
            searchlist = self.search.get_list_of_elements(self.heading)
            expname = []
            for i in searchlist:
                expname.append(i.text)
            print(expname)
        except TimeoutException:
            print("search list is not loading")
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

        try:
            assert "TEST LIVE EXP (NEW YORK)" in expname
            self.search.click_element(BasePage.HOME)
            time.sleep(3)

        except AssertionError:
            # Create a unique timestamp for the screenshot
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
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.searchexp
    def test_search_by_namesearch_page(self, request):

        self.search = SearchExp(self.driver)
        self.search.search_exp_by_name_on_search_page("Test live exp")
        time.sleep(8)

        try:
            searchlist = self.search.get_list_of_elements(self.heading)
            expname = []
            for i in searchlist:
                expname.append(i.text)
            print(expname)
        except TimeoutException:
            print("search list is not loading")
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

        try:
            assert "TEST LIVE EXP (NEW YORK)" in expname
            self.search.click_element(BasePage.HOME)
            time.sleep(3)

        except AssertionError:
            # Create a unique timestamp for the screenshot
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
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.searchexp
    def test_search_by_name_category_search_page(self, request):

        self.search = SearchExp(self.driver)
        self.search.search_exp_by_name_category_on_search_page("Test live exp")
        time.sleep(8)

        try:
            searchlist = self.search.get_list_of_elements(self.heading)
            expname = []
            for i in searchlist:
                expname.append(i.text)
            print(expname)
        except TimeoutException:
            print("search list is not loading")
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

        try:
            assert "TEST LIVE EXP (NEW YORK)" in expname
            self.search.click_element(BasePage.HOME)
            time.sleep(3)

        except AssertionError:
            # Create a unique timestamp for the screenshot
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
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise
