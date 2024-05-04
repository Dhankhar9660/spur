import os
import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Search_experiences import SearchExp


class TestSearchPage(BaseTest):
    policy = (By.XPATH, "//h2[@class='termsHeading']")
    results = (By.XPATH, "//div[@class='wsa_list_head']")
    heading = (By.XPATH, "//h2//a")
    expheading = (By.XPATH, "//div[@class='nexExp_heading']")
    exphead = (By.XPATH, "//div[@class='newExpDetail_head']")
    price = (By.XPATH, "//div[@class='newExpPrice ng-star-inserted']")

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
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

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
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

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
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

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
            directory = "C:/Users/Bal/PycharmProjects/spur-automations/Screenshot"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            self.search.click_element(BasePage.HOME)
            time.sleep(3)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.expdetails
    def test_exp_details_page(self):

        self.details = SearchExp(self.driver)
        self.details.exp_details_from_home_page("Test live exp")
        time.sleep(8)

        try:
            expheading = self.details.get_element_text(self.expheading)
            expname = self.details.get_element_text(self.exphead)
            expprice = self.details.get_element_text(self.price)
        except TimeoutException:
            print("details page elements are not loading")
            self.details.click_element(BasePage.HOME)
            time.sleep(3)
            raise
        try:
            assert "Test live exp" == expheading
            self.details.click_element(BasePage.HOME)
            time.sleep(3)
        except AssertionError:
            self.details.click_element(BasePage.HOME)
            print("Page heading not loading")
            raise
        try:
            assert "Test live exp" == expname
        except AssertionError:
            print("Experience name is not loading")
            raise
        try:
            assert "$110 { Per Group }" == expprice
        except AssertionError:
            print("Experience price is not loading")
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.expdetails
    def test_exp_details_page_from_location_search(self):

        self.details = SearchExp(self.driver)
        self.details.search_by_location("New york", "Test live exp")
        time.sleep(8)

        try:
            expheading = self.details.get_element_text(self.expheading)
            expname = self.details.get_element_text(self.exphead)
            expprice = self.details.get_element_text(self.price)
        except TimeoutException:
            print("details page elements are not loading")
            self.details.click_element(BasePage.HOME)
            time.sleep(3)
            raise
        try:
            assert "Test live exp" == expheading
            self.details.click_element(BasePage.HOME)
            time.sleep(3)
        except AssertionError:
            self.details.click_element(BasePage.HOME)
            print("Page heading not loading")
            raise
        try:
            assert "Test live exp" == expname
        except AssertionError:
            print("Experience name is not loading")
            raise
        try:
            assert "$110 { Per Group }" == expprice
        except AssertionError:
            print("Experience price is not loading")
            raise
