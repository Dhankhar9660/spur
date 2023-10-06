import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CmsPage(BasePage):
    # Create Locators for elements on Login Page:
    privacy = "//footer//a[text()='privacy policy']"
    terms = "//footer//a[text()='terms of use']"
    contactemail = "//div[@id='designstudio-button']//button"
    FAQs = "//a[text()='FAQs']"
    find_couple = "(//a[text() = 'Find a Couple'])[1]"
    searchinput = (By.XPATH, "//input[@id='couplefind']")

    # Constructor for this class :
    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    def search_ticket(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("as")
