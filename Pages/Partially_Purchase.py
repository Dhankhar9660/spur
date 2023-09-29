import time
import re

import pyperclip
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData


class PartiallyPurchase(BasePage):
    Add_Experience = (By.XPATH, "//a[text() = 'Add EXPERIENCES']")
    Price_Filter = (By.XPATH, "(//ul[@class = 'filter_typeoption']//li)[5]")
    Click_Add_Registry = (By.XPATH, "(//button[text() = ' Add to registry '])[1]")
    Click_Partally_Purchase = (By.XPATH, "(//a[text() = 'PARTIAL PURCHASE'])[1]")
    Click_Partally_Purchase_Hidden = "(//a[text() = 'PARTIAL PURCHASE'])[1]"
    Add_To_Basket = (By.XPATH, "(//a[text() = 'ADD TO CART'])[2]")
    Price = (By.XPATH, "(//i[@class = 'bigPrice'])[2]")
    exp_name = (By.XPATH, "(//div[@class = 'SelectExpCoupleBody']//li//h2)[1]")
    Click_exp_Hidden = "(//div[@class = 'SelectExpCoupleBody']//li//h2)[1]"
    Unit_Price = (By.XPATH, "(//i[@class = 'bigPrice'])[2]")
    Exp_Price = (By.XPATH, "(//p[@class = 'purRate'])[2]")
    Unit = (By.XPATH, "//a[text() = '7']")
    Total_Price = (By.XPATH, "//span[@class = 'cartPriceTotal ng-star-inserted']")
    Cart_Price = (By.XPATH, "//div[@class='priceCartsubtotal']//span")
    Click_Outside = (By.XPATH, "//div/label[text() = 'Search By Category/Name']")
    Exp_name = (By.XPATH, "(//div[@class = 'bottomDesInter']//a)[1]")
    Exp_Dropdown = (By.XPATH, "//div[@id = 'ej2_dropdownlist_0_popup']")
    Search_Exp = (By.LINK_TEXT, "Cooking Class")
    Hover_On_Exp = (By.XPATH, "//div[@class = 'product-image lazyloaded']")
    Remove_Registry = (By.XPATH, "//a[text() = 'Remove from registry']")

    def __int__(self, driver):
        super().__init__(driver)

    def Partialy_Purchase(self):

        self.click_element(self.Add_Experience)
        time.sleep(5)
        self.click_element(self.Price_Filter)
        time.sleep(2)
        list = (By.XPATH, "//div[starts-with(text(), ' $')]")

        all_price = self.get_list_of_elements(list)
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
            print('price range does not match')
            raise
        time.sleep(2)
