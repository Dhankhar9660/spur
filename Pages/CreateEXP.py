import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
# from datetime import datetime
import datetime


class CreateExp(BasePage):
    # Create Locators for elements on Add new experience Page:
    Summeryinput = (By.XPATH, "//textarea[@formcontrolname='summary']")
    Detailsinput = (By.XPATH, "//textarea[@formcontrolname='details']")
    Included = (By.XPATH, "(//input[@class='form-control'])[1]")
    Excluded = (By.XPATH, "(//input[@class='form-control'])[2]")
    priceamount = (By.XPATH, "(//input[@formcontrolname='price'])")
    Tax = (By.XPATH, "(//input[@formcontrolname='tax'])")

    exp_name = "test auto " + datetime.datetime.now().strftime("%H%M%S%B%d%Y")

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions
    def createexp(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(2)
        self.click_on_hidden_element(BasePage.ADDNEWEXP)
        time.sleep(3)
        self.send_keys(BasePage.EXPNAMEINPUT, self.exp_name)
        self.send_keys(self.Summeryinput, BasePage.Summery)
        self.send_keys(self.Detailsinput, BasePage.Details)
        self.click_on_hidden_element(BasePage.NEXT2)
        time.sleep(4)
        self.send_keys(self.Included, BasePage.Include)
        self.send_keys(self.Excluded, BasePage.Exclude)
        self.click_on_hidden_element(BasePage.NEXT3)
        # time.sleep(3)
        self.send_keys(self.priceamount, BasePage.Price)
        self.send_keys(self.Tax, BasePage.Tex)
        self.click_on_hidden_element(BasePage.NEXT3)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.NEXT3)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.NEXT3)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.NEXT3)
        time.sleep(3)
        self.click_on_hidden_element(BasePage.NEXT3)

        # # self.driver.execute_script("window.scrollTo(0, 400)")
        #
        # self.send_keys(BasePage.INCLUDE, BasePage.Include)
        # self.send_keys(BasePage.EXCLUDE, BasePage.Exclude)
        # self.click_element(BasePage.NEXT3)
        # self.send_keys(BasePage.SEASION, BasePage.Seasion)
        # self.send_keys(BasePage.DAYS, BasePage.Days)
        # self.click_element(BasePage.NEXT3)
        # self.click_element(BasePage.SAMEADD)
        # self.click_element(BasePage.NEXT3)
        # self.send_keys(BasePage.PRICE, BasePage.Price)
        # self.send_keys(BasePage.TEX, BasePage.Tex)
        # self.click_element(BasePage.NEXT3)
        # self.click_element(BasePage.REDIO_NO)
        # self.click_element(BasePage.NEXT3)
        # time.sleep(2)
        # self.click_element(BasePage.NEXT3)
        # time.sleep(3)
        # self.click_element(BasePage.NEXT3)
        # time.sleep(4)
        # self.driver.execute_script("window.scrollTo(0, 400)")
        # self.click_element(BasePage.NEXT3)
        # time.sleep(4)
        # self.driver.execute_script("window.scrollTo(0, 500)")
        # # self.click_element(BasePage.SUBMIT)
