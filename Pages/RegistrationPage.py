"""Author: Balkishan Dhankhar"""

import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import random
from datetime import datetime


class Registration(BasePage):
    # Create Locators for elements on Registration Page:
    Wedding_cup_reg = (By.XPATH, "(//div[@class='dnt_div']//a)[1]")
    Wedding_email = (By.XPATH, "//input[@id='email']")
    Wedding_password = (By.XPATH, "//input[@id='passwrd']")
    Lets_do_this = (By.XPATH, "//button[@class='form-control submit-button']")

    First_name = (By.XPATH, "//input[@id='first_name']")
    Last_name = (By.XPATH, "//input[@id='last_name']")
    Partner_fname = (By.XPATH, "//input[@id='partner_first_name']")
    Partner_lname = (By.XPATH, "//input[@id='partner_last_name']")
    Wedding_date = (By.XPATH, "//input[@id='wedding_date']")
    Selectseason = (By.XPATH, "//select[@id='season_options']")
    Season = (By.XPATH, "(//option[@class='ng-star-inserted'])[2]")
    Robot = (By.XPATH, "//div[@class='rc-anchor-content']")
    Submit2 = (By.XPATH, "//button[@class='form-control submit-button']")

    FNAME = "Test"
    LNAME = "Tester"
    PFARST_NAME = "Semi"
    PLAST_NAME = "Wara"
    DATE = "03/09/2022"

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    email = "Test" + dt_string + "@gmail.com"
    password = "System@123"

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions :

    def Regist(self):
        self.click_element(BasePage.LOGIN_ICON)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_element(self.Wedding_cup_reg)
        self.send_keys(self.Wedding_email, self.email)
        self.send_keys(self.Wedding_password, self.password)
        time.sleep(3)
        self.click_element(self.Lets_do_this)
        self.send_keys(self.First_name, self.FNAME)
        self.send_keys(self.Last_name, self.LNAME)
        self.send_keys(self.Partner_fname, self.PFARST_NAME)
        self.send_keys(self.Partner_lname, self.PLAST_NAME)
        # self.send_keys(self.Wedding_date, self.DATE)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.Selectseason)
        time.sleep(1)
        self.click_element(self.Season)
        time.sleep(1)
        # self.click_element(self.Robot)
        # time.sleep(3)
        self.click_element(self.Submit2)
