import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CreateExp(BasePage):
    # Create Locators for elements on Add new experience Page:

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def Createexp(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(2)
        self.click_element(BasePage.ADDNEWEXP)
        time.sleep(3)
        self.send_keys(BasePage.EXPNAMEINPUT, BasePage.EXP_Name)
        self.click_element(BasePage.NEXT2)
        self.send_keys(BasePage.SUMMERY, BasePage.Summery)
        self.click_element(BasePage.NEXT3)
        time.sleep(3)
        self.send_keys(BasePage.DETAILS, BasePage.Details)
        # self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_element(BasePage.NEXT3)
        self.send_keys(BasePage.INCLUDE, BasePage.Include)
        self.send_keys(BasePage.EXCLUDE, BasePage.Exclude)
        self.click_element(BasePage.NEXT3)
        self.send_keys(BasePage.SEASION, BasePage.Seasion)
        self.send_keys(BasePage.DAYS, BasePage.Days)
        self.click_element(BasePage.NEXT3)
        self.click_element(BasePage.SAMEADD)
        self.click_element(BasePage.NEXT3)
        self.send_keys(BasePage.PRICE, BasePage.Price)
        self.send_keys(BasePage.TEX, BasePage.Tex)
        self.click_element(BasePage.NEXT3)
        self.click_element(BasePage.REDIO_NO)
        self.click_element(BasePage.NEXT3)
        time.sleep(2)
        self.click_element(BasePage.NEXT3)
        time.sleep(3)
        self.click_element(BasePage.NEXT3)
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_element(BasePage.NEXT3)
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 500)")
        # self.click_element(BasePage.SUBMIT)
