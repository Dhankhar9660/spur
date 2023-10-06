""" Test Page for Login Checks"""
import os
import time
import sys
import pytest

from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
import openpyxl
from datetime import datetime


class Test_Login(BaseTest):
    # ______________create method for Login and create all login test cases____________________
    @pytest.mark.login
    @pytest.mark.alltest
    def test_check_with_blank(self, request):

        self.asd = LoginPage(self.driver)
        self.asd.login("", "")
        try:
            errormessage = self.asd.get_element_text(BasePage.LOGIN_EMAIL_VALIDATION)
            passerror = self.asd.get_element_text(BasePage.LOGIN_PASSWORD_VALIDATION)
        except TimeoutError:
            print("page loading time is too high.")
            raise
        try:
            assert errormessage == BasePage.Email_error_message
            assert passerror == BasePage.Password_error_message
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
            raise

    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.new
    def test_couple_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True
            time.sleep(3)

        except AssertionError:
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

        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)
            assert all(x == y for x, y in zip(TestData.menuoption_couple, menulist))
            self.login.click_element(BasePage.LOGOUT)
            print("Couple user login working fine.")
            time.sleep(3)
        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.alltest
    def test_couple_login_by_username(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_USER_NAME, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True
            time.sleep(3)

        except AssertionError:
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

        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)
            assert all(x == y for x, y in zip(TestData.menuoption_couple, menulist))
            self.login.click_element(BasePage.LOGOUT)
            print("Couple user login working fine.")
            time.sleep(3)
        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.alltest
    def test_individual_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.INDIVIDUAL_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True

        except AssertionError:
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

        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_individual, menulist))
            print("Individual user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_EP_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.EP_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)

        try:
            assert flag == True
        except AssertionError:
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
        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_ep, menulist))
            print("EP user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.alltest
    def test_charity_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.CHARITY_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True
        except AssertionError:
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

        try:
            try:
                menu = (By.XPATH, "//span[@class='menuName']")
                menuoption = self.login.get_list_of_elements(menu)
            except TimeoutError:
                print("Element not found, please check locator!!")

            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_charity, menulist))
            print("Charity user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_joy_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.JOY_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        accept = (By.XPATH, "//button[@class='btn btn-accept']")
        self.login.click_element(accept)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True

        except AssertionError:
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

        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)
            assert all(x == y for x, y in zip(TestData.menuoption_joy, menulist))
            print("Joy user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.alltest
    def test_zola_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.ZOLA_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        accept = (By.XPATH, "//button[@class='btn btn-accept']")
        self.login.click_element(accept)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True
        except AssertionError:
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

        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_joy, menulist))
            print("Zola user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
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

    @pytest.mark.login
    @pytest.mark.alltest
    @pytest.mark.regression
    def test_knot_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.KNOT_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        accept = (By.XPATH, "//button[@class='btn btn-accept']")
        self.login.click_element(accept)
        mydashboard = (By.XPATH, "(//a[text()='My Dashboard'])[1]")
        flag = self.login.is_visible(mydashboard)
        try:
            assert flag == True

            time.sleep(3)
        except AssertionError:
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
        try:
            menu = (By.XPATH, "//ul[@class='navbar-nav ml-auto']//li//a")
            menuoption = self.login.get_list_of_elements(menu)
            menulist = []
            for name in menuoption:
                menulist.append(name.text)

            assert all(x == y for x, y in zip(TestData.menuoption_joy, menulist))
            print("Knot user login working fine.")
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)

        except AssertionError:
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
