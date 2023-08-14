from datetime import datetime
import time
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Config.config import TestData


class RegistryPage(BasePage):
    # Create Locators for elements on Login Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions :

    def registry(self):
        # self.click_element(BasePage.DASHBOARD)
        self.click_element(BasePage.ADDEXP)
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(6)
        self.click_element(BasePage.EXPERIENCE)
        time.sleep(3)

    def Add_Registry(self, expname, actual_exp):

        self.click_element(BasePage.Click_Home)
        self.send_keys(BasePage.Search_Box, expname)
        self.click_on_hidden_element(BasePage.Click_Search)
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//h2//a")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            Product_Name = self.get_element_text(BasePage.Product_Name)
            print(Product_Name)
            assert Product_Name == actual_exp
            self.click_on_hidden_element(BasePage.Click_On_Product)
        except AssertionError:
            print('Product name not found')
            raise
        self.click_on_hidden_element(BasePage.Add_To_Registry)
        self.click_element(BasePage.Click_MyDashboard)
        time.sleep(3)

    # ---------------- Remove from registry after add to registry _____________
    def Remove_From_Registry(self, expname, actual_exp):

        self.click_element(BasePage.HOME)
        self.send_keys(BasePage.Search_Box, expname)
        self.click_on_hidden_element(BasePage.Click_Search)
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//h2//a")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            Product_Name = self.get_element_text(BasePage.Product_Name)
            assert Product_Name == actual_exp
            self.click_on_hidden_element(BasePage.Click_On_Product)
        except AssertionError:
            print('Product name not found')
            raise
        self.click_on_hidden_element(BasePage.Remove_From_Registry)
        time.sleep(2)
