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
    # create method for Login and create object of Test_Login to access various functions from Parent Class and check all login test cases
    @pytest.mark.login
    @pytest.mark.alltest
    def test_check_with_blank(self, request):

        self.asd = LoginPage(self.driver)
        self.asd.login("", "")

        errormessage = self.asd.get_element_text(BasePage.LOGIN_EMAIL_VALIDATION)
        passerror = self.asd.get_element_text(BasePage.LOGIN_PASSWORD_VALIDATION)
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
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_couple_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            time.sleep(3)
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_individual_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.INDIVIDUAL_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_EP_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.EP_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

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
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_joy_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.JOY_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)

            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_zola_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.ZOLA_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.login
    @pytest.mark.alltest
    def test_knot_login(self, request):

        self.login = LoginPage(self.driver)
        self.login.login(BasePage.KNOT_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)
        flag = self.login.is_visible(BasePage.LOGOUT)
        try:
            assert flag == True
            self.login.click_element(BasePage.LOGOUT)
            time.sleep(3)
        except AssertionError:
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/Spurowebest/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise
