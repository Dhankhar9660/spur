import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class SearchExp(BasePage):
    # Create Locators for elements on Login Page:
    privacy = "//footer//a[text()='privacy policy']"
    searchicon = (By.XPATH, "//button[@class='primeSeach prime_active']")
    search = "//button[@class='primeSeach prime_active']"
    name_input = (By.XPATH, "//input[@placeholder='Title']")
    location_input = (By.XPATH, "//input[@placeholder='Search Location...']")
    letsgo_button = (By.XPATH, "//div[@class='filterDropdownList']//input[@type= 'submit']")
    SearchByinput = (By.XPATH, "//input[@placeholder='Find by Name/Category']")

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    def search_exp_by_name_on_home(self, exp_name):
        self.send_keys(BasePage.SEARCHBOXEXP, exp_name)
        time.sleep(2)
        self.click_element(self.searchicon)

    def search_exp_by_name_and_location(self, exp_name, location):
        self.click_on_hidden_element(self.search)
        self.send_keys(self.name_input, exp_name)
        self.send_keys(self.location_input, location)
        time.sleep(1)
        self.driver.find_element(*self.location_input).send_keys(Keys.DOWN)
        self.driver.find_element(*self.location_input).send_keys(Keys.ENTER)
        self.click_element(self.letsgo_button)

    def search_exp_by_name_on_search_page(self, exp_name):
        self.click_on_hidden_element(self.search)
        self.send_keys(self.name_input, exp_name)
        self.click_element(self.letsgo_button)

    def search_exp_by_name_category_on_search_page(self, exp_name):
        self.click_on_hidden_element(self.search)
        self.send_keys(self.SearchByinput, exp_name)
        time.sleep(2)
        self.driver.find_element(*self.location_input).send_keys(Keys.DOWN)
        self.driver.find_element(*self.location_input).send_keys(Keys.ENTER)
