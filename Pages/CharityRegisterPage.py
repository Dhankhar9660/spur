from datetime import datetime
import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CharityregPage(BasePage):
    # Create Locators for elements on Login Page:
    Charity_register = (By.XPATH, "(//div[@class='dnt_div']//a)[4]")
    Getstarted = (By.XPATH, "//button[@class='form-control submit-button']")
    Email = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='passwrd']")
    Username = (By.XPATH, "//input[@id='username']")
    Fname = (By.XPATH, "//input[@formcontrolname='first_name']")
    Lname = (By.XPATH, "//input[@formcontrolname='last_name']")
    Phone = (By.XPATH, "//input[@id='phone']")
    Charityname = (By.XPATH, "//input[@id='title']")
    Number = (By.XPATH, "//input[@id='number']")
    Website = (By.XPATH, "//input[@id='website']")
    Category = (By.XPATH, "(//option[@class='ng-star-inserted'])[1]")
    Summary = (By.XPATH, "//textarea[@formcontrolname='summary']")
    Next = (By.XPATH, "//input[@class='twobtns-accept']")
    Next1 = (By.XPATH, "//button[@class='twobtns-accept']")
    Details = (By.XPATH, "//textarea[@formcontrolname='description']")
    Address = (By.XPATH, "//input[@id='shipping_address_1']")
    City = (By.XPATH, "//input[@id='shipping_city']")
    State = (By.XPATH, "//input[@id='shipping_state']")
    Zip = (By.XPATH, "//input[@id='shipping_postcode']")
    Complete = (By.XPATH, "//input[@class='twobtns-accept']")
    Contrycode = (By.XPATH, "//input[@id='country-search-box']")
    indcode = (By.XPATH, "//span[text()='India (भारत)']")
    cclist = (By.XPATH, "//div[@class='iti__flag-container']")

    now = datetime.now()
    dt_string = now.strftime("%d%m%M%S")
    EMAIL = "test" + dt_string + "@yopmail.com"
    PASSWORD = "System@123"
    USERID = "USER" + dt_string
    FNAME = "TEST"
    LNAME = "CHARITY"
    PHONE = "9999999998"
    CHARITYNAME = "TESTCHARITY"
    NUMBER = "9898989898"
    WEBSITE = "WWW.Test.com"
    SUMMARY = "This charity only for testing" \
              "This charity only for testing" \
              "This charity only for testing"
    DETAILS = "This charity only for testing" \
              "This charity only for testing" \
              "This charity only for testing" \
              "This charity only for testing"
    ADDRESS = "New York , USA"
    CITY = "New York"
    STATE = "New York"
    ZIP = "90090"

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    # Page actions :

    def charityregister(self):
        self.click_element(BasePage.LOGIN_ICON)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_element(self.Charity_register)
        self.click_element(self.Getstarted)
        self.send_keys(self.Email, self.EMAIL)
        self.send_keys(self.Password, self.PASSWORD)
        self.send_keys(self.Username, self.USERID)
        time.sleep(2)
        self.click_element(self.Getstarted)
        time.sleep(3)
        self.send_keys(self.Fname, self.FNAME)
        self.send_keys(self.Lname, self.LNAME)
        self.click_element(self.cclist)
        self.click_element(self.indcode)
        self.send_keys(self.Phone, self.PHONE)
        self.click_element(self.Getstarted)
        time.sleep(3)
        self.send_keys(self.Charityname, self.CHARITYNAME)
        self.send_keys(self.Number, self.NUMBER)
        self.send_keys(self.Website, self.WEBSITE)
        self.click_element(self.Category)
        self.click_element(self.Next1)
        time.sleep(3)
        self.send_keys(self.Summary, self.SUMMARY)
        self.click_element(self.Next)
        time.sleep(3)
        self.send_keys(self.Details, self.DETAILS)
        self.click_element(self.Next)
        self.send_keys(self.Address, self.ADDRESS)
        self.send_keys(self.City, self.CITY)
        self.send_keys(self.State, self.STATE)
        self.send_keys(self.Zip, self.ZIP)
        self.click_element(self.Next1)
        time.sleep(3)
        self.click_element(self.Complete)
        time.sleep(5)
