from datetime import datetime
import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ExpproPage(BasePage):
    # Create Locators for elements on Login Page:
    Exp_pro_register = (By.XPATH, "(//div[@class='dnt_div']//a)[3]")
    Accept = (By.XPATH, "//input[@class='twobtns-accept']")
    Company_name = (By.XPATH, "//input[@id='company_name']")
    Website = (By.XPATH, "//input[@id='website']")
    Email = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='passwrd']")
    Userid = (By.XPATH, "//input[@id='username']")
    First_name = (By.XPATH, "//input[@id='first_name']")
    Last_name = (By.XPATH, "//input[@id='last_name']")
    cclist = (By.XPATH, "//div[@class='iti__flag-container']")
    Contrycode = (By.XPATH, "//input[@id='country-search-box']")
    indcode = (By.XPATH, "//span[text()='India (भारत)']")
    Phone_number = (By.XPATH, "//input[@id='phone']")
    Address = (By.XPATH, "//input[@id='shipping_address_1']")
    City = (By.XPATH, "//input[@id='shipping_city']")
    State = (By.XPATH, "//input[@id='shipping_state']")
    Zip = (By.XPATH, "//input[@id='shipping_postcode']")
    Next_button = (By.XPATH, "//input[@class='twobtns-accept']")

    # variable
    COMPANY_NAME = "TESTING"
    WEBSITE = "WWW.AUTOMETION.COM"
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    USERID = "TEST" + dt_string
    EMAIL_EXP = "Test" + dt_string + "@yopmail.com"
    PASWORD = "System@123"
    FNAME = "TEST"
    LNAME = "TESTLAST"
    PHONE = "8888999989"
    ADDRESS = "USA USA USA"
    CITY = "NEW YORK"
    STATE = "NEW YORK"
    ZIP = "90090"

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions :

    def expregister(self):
        self.click_element(BasePage.LOGIN_ICON)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_element(self.Exp_pro_register)
        self.click_element(self.Accept)
        time.sleep(3)
        self.click_element(self.Accept)
        time.sleep(2)
        self.click_element(self.Accept)
        time.sleep(2)
        self.send_keys(self.Company_name, self.COMPANY_NAME)
        self.send_keys(self.Website, self.WEBSITE)
        self.send_keys(self.Email, self.EMAIL_EXP)
        self.send_keys(self.Password, self.PASWORD)
        self.send_keys(self.Userid, self.USERID)
        self.send_keys(self.First_name, self.FNAME)
        self.send_keys(self.Last_name, self.LNAME)
        self.click_element(self.cclist)
        self.click_element(self.indcode)
        # self.send_keys(self.Contrycode, self.CCODE)
        self.send_keys(self.Phone_number, self.PHONE)
        self.send_keys(self.Address, self.ADDRESS)
        self.send_keys(self.City, self.CITY)
        self.send_keys(self.State, self.STATE)
        self.send_keys(self.Zip, self.ZIP)
        self.click_element(self.Next_button)
