import time
import os
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
    productlist = (By.XPATH, "//div[@class='item-box']")
    # productname = (By.XPATH, "//h2[@class='product-title']")
    nextpage = (By.XPATH, "//li[@class='next-page']")

    def test_addtocart(self, request):
        self.asd = LoginPage(self.driver)
        product_elements = self.asd.get_list_of_elements(self.productlist)
        for product in product_elements:
            product_name_element = product.find_element(By.XPATH, ".//h2[@class='product-title']")
            product_name = product_name_element.text
            print("name == " + product_name)
            if product_name == "Wool Hat":
                add_to_cart_button = product.find_element(By.XPATH, ".//input[@value='Add to cart']")
                add_to_cart_button.click()
                break

            else:
                self.nextpage.click()

        time.sleep(15)
        print("Test case is completed......")
