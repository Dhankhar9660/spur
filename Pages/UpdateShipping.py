import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage



class Shipping(BasePage):
    def __int__(self, driver):
        super.__init__(driver)

    def UpdateShipping(self, Fname, Lname, address, country):

        self.click_element(BasePage.Setting)
        time.sleep(5)
        self.click_element(BasePage.Shipping)
        self.clear_text_box(BasePage.FirstName)
        self.send_keys(BasePage.FirstName, Fname)
        self.clear_text_box(BasePage.LastName)
        self.send_keys(BasePage.LastName, Lname)
        self.clear_text_box(BasePage.Address)
        self.send_keys(BasePage.Address, address)
        self.click_element(BasePage.Country)
        self.send_keys(BasePage.Search_Country, country)
        counteries = self.driver.find_elements(By.XPATH, "//ul[@role = 'listbox']/li")
        for country in counteries:

            if country.text == "Aruba":
                country.click()
                break
        time.sleep(1)
        self.click_on_hidden_element(BasePage.Click_Update)
        time.sleep(4)
