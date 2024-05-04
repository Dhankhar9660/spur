""" Test Page for Login Checks"""
import os
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from datetime import datetime
from selenium.common.exceptions import TimeoutException


class TestHomepage(BaseTest):
    # ______________create method for Login and create all home page test cases____________________
    header_link = (By.XPATH, "(//ul[@id='accordionHeadMenu'])[1]/child::li")
    category_list = (By.XPATH, "//div[@class='categoryCard']//span")
    destination_list = (By.XPATH, "(//owl-stage)[1]//span")
    book_now = "//span[text()='BOOK NOW']"
    location_input = (By.XPATH, "//div[@class='formToggleCard']//input[@role='searchbox']")
    location = "new york city"
    date_picker = "//div[@class='formToggleCard']//input[@placeholder='Select Date']"
    today_date = datetime.today().date()
    datenew = datetime.today().strftime('%m-%d-%Y')
    formatted_date = datetime.today().strftime('%d')
    date = f"//bs-datepicker-container//bs-calendar-layout//span[text()='{formatted_date}']"
    search_button = "(//button[@class='newMobSubmit'])[1]"

    @pytest.mark.homepage
    @pytest.mark.alltest
    def test_nav_link(self, request):
        base_page = BasePage(self.driver)

        try:
            page_nave_link_list = base_page.get_list_of_elements(self.header_link)
            link_name = []
            for i in page_nave_link_list:
                link_name.append(i.text)
            link_name = [item for item in link_name if item.strip()]
            print(link_name)
        except TimeoutException:
            print("page loading time is too high.")
            raise
        try:
            actual_links = ['HOME', 'LOCATIONS', 'EXPERIENCES', 'GIFT IDEAS', 'TICKETS', 'WEDDING REGISTRY', 'ABOUT',
                            'FIND A COUPLE']
            assert actual_links == link_name
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
            raise

    @pytest.mark.homepage
    @pytest.mark.alltest
    def test_page_title(self, request):

        try:
            page_title = self.driver.title
            print(page_title)
        except TimeoutException:
            print("page loading time is too high.")
            raise
        try:
            assert page_title == "Home"
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
            raise

    @pytest.mark.homepage
    @pytest.mark.alltest
    def test_popular_category(self, request):
        base_page = BasePage(self.driver)

        try:
            category_list = base_page.get_list_of_elements(self.category_list)
            category_name = []
            for i in category_list:
                category_name.append(i.text)

        except TimeoutException:
            print("page loading time is too high.")
            raise
        try:
            category = ['Food and drink', 'Flying', 'Animals', 'Health and Wellness', 'Water Sports', 'City Tours']
            assert category == category_name
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
            raise

    @pytest.mark.homepage
    @pytest.mark.alltest
    def test_popular_destination(self):
        base_page = BasePage(self.driver)

        try:
            destination_list = base_page.get_list_of_elements(self.destination_list)
            destination_name = []
            for i in destination_list:
                destination_name.append(i.text)
        except TimeoutException:
            print("destination list loading time is too high.")
            raise

    def test_search_new(self):
        try:
            base_page = BasePage(self.driver)
            base_page.click_on_hidden_element(self.book_now)
            base_page.send_keys(self.location_input, self.location)
            time.sleep(4)
            self.driver.find_element(*self.location_input).send_keys(Keys.DOWN)
            self.driver.find_element(*self.location_input).send_keys(Keys.ENTER)
            base_page.click_on_hidden_element(self.date_picker)
            base_page.click_on_hidden_element(self.date)
            base_page.click_on_hidden_element(self.search_button)
            time.sleep(5)
        except TimeoutException:
            print("search from not working on home page for book now")
            raise

        try:
            url = self.driver.current_url
            assert url == (f"https://spurexperiences.com/experience-search-booking?location=new-york-new-york&category"
                           f"=&date={self.datenew}&is_booking=1")

        except ModuleNotFoundError:
            raise
