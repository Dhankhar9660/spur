import time

import pytest
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.by import By
from Pages.RegistryPage import RegistryPage
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Partially_Purchase import PartiallyPurchase


class Test_PartiallyPurchase(BaseTest):

    @pytest.mark.patial_purchase
    @pytest.mark.alltes
    def test_partiallypurchase(self):
        login = LoginPage(self.driver)
        login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(5)

        self.purchase = PartiallyPurchase(self.driver)
        self.purchase.Partialy_Purchase()
        time.sleep(3)
        exp = self.purchase.get_element_text(PartiallyPurchase.exp_name)
        Exp = str(exp)
        Exp_Name = Exp.split('(')[0]
        self.purchase.click_on_hidden_element(PartiallyPurchase.Click_exp_Hidden)
        time.sleep(1)
        self.purchase.click_element(PartiallyPurchase.Click_Add_Registry)
        time.sleep(1)
        self.purchase.click_element(BasePage.Click_MyDashboard)
        time.sleep(3)

        self.purchase.click_element(BasePage.View_Our_Url)
        time.sleep(1)
        self.purchase.click_element(BasePage.Copy_Url)

        clipboard_text = pyperclip.paste()

        self.purchase.click_element(BasePage.Close_Popup)
        self.purchase.click_element(BasePage.Log_Out)
        time.sleep(2)

        self.purchase.driver.get(clipboard_text)
        time.sleep(5)

        self.purchase.driver.execute_script("window.scrollTo(0,900)")
        self.purchase.send_keys(BasePage.Search_Product, Exp_Name.title())
        time.sleep(3)
        self.purchase.click_element(BasePage.Search)
        time.sleep(5)

        self.purchase.driver.execute_script("window.scrollTo(0,1000)")

        try:
            Exp_name = self.purchase.get_element_text(PartiallyPurchase.Exp_name)
            Exp_name1 = Exp_name.split('(')[0]
            assert Exp_name1 == Exp_Name
            self.purchase.click_on_hidden_element(PartiallyPurchase.Click_Partally_Purchase_Hidden)

        except AssertionError:
            print('Experience is not found')
            raise
        time.sleep(2)

        Exp_Price = self.purchase.get_element_text(PartiallyPurchase.Exp_Price)
        ExpPrice = eval(Exp_Price.strip("${ ").split(" ")[0])
        print(ExpPrice)
        Price = self.purchase.get_element_text(PartiallyPurchase.Unit_Price)
        Unit_Price = eval(Price.split('$')[1])

        try:
            assert ExpPrice / 10 == Unit_Price
            print('value matched')
        except Exception as e:
            print('value does not matched', e)
            raise

        self.purchase.click_element(PartiallyPurchase.Unit)
        time.sleep(2)
        Price = self.purchase.get_element_text(PartiallyPurchase.Total_Price)
        Total_Price = eval(Price.split('$')[1])

        try:
            assert Unit_Price * 7 == Total_Price
            print('price matched')
        except Exception as e:
            print('price not matched', e)
            raise

        self.purchase.click_element(PartiallyPurchase.Add_To_Basket)
        time.sleep(2)
        self.purchase.driver.refresh()
        time.sleep(2)
        self.purchase.click_element(BasePage.Click_On_Cart)

        try:
            Cart_Price = self.purchase.get_element_text(PartiallyPurchase.Cart_Price)
            print(Cart_Price)
            Price = eval(Cart_Price.split('$')[1])
            assert Price == Unit_Price * 7
        except Exception as e:
            print('price not matched', e)
            raise

        try:
            Experience_Name = self.purchase.get_element_text(BasePage.Product)
            assert Experience_Name + " " == Exp_Name
            self.purchase.click_element(BasePage.Remove_From_Cart)
            self.purchase.click_element(BasePage.Click_Yes_Button)
        except AssertionError:
            print('Product not found')
            raise
        time.sleep(3)

        # ----Remove from registry-----
        self.login = LoginPage(self.driver)
        self.login.login(BasePage.COUPLE_EMAIL, BasePage.AUTOMATION_PASSWORD)
        time.sleep(2)
        # self.purchase.driver.get(clipboard_text)
        time.sleep(5)
        self.purchase.click_element(BasePage.Click_MyDashboard)
        self.purchase.driver.execute_script("window.scrollTo(0,1000)")
        self.purchase.hover_element(PartiallyPurchase.Hover_On_Exp)
        time.sleep(2)
        self.purchase.click_element(PartiallyPurchase.Remove_Registry)
        time.sleep(2)
        self.purchase.click_element(BasePage.Log_Out)
