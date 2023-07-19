import time
import os
import sys
import pytest

from openpyxl import load_workbook
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
import openpyxl
from datetime import datetime


class Test_Login(BaseTest):
    productlist = (By.XPATH, "//div[@class='item-box']")
    productname = (By.XPATH, "//h2[@class='product-title']")
    next_button = (By.XPATH, "//li[@class='next-page']")

    def test_searchproduct(self, request):
        self.asd = LoginPage(self.driver)
        pro_list = []
        while True:
            product_elements = self.asd.get_list_of_elements(self.productlist)
            for product in product_elements:
                product_name_element = product.find_element(By.XPATH, ".//h2[@class='product-title']")
                product_name = product_name_element.text
                pro_list.append(product_name)
                # print("name == " + product_name)
                if product_name == "Men's Wrinkle Free Long Sleeve":
                    add_to_cart_button = product.find_element(By.XPATH, ".//input[@value='Add to cart']")
                    add_to_cart_button.click()
                    time.sleep(2)
                    print("Test case is completed......")
                    return
            next_button_element = None
            try:
                next_button_element = self.asd.driver.find_element(By.XPATH, "//li[@class='next-page']")
            except NoSuchElementException:
                pass

            if next_button_element and "Men's Wrinkle Free Long Sleeve" not in pro_list:
                next_button_element.click()
                time.sleep(3)
            else:
                print("Item not available, please search with other product's name!!!!")
                break
