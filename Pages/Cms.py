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

    def about(self):
        self.hover_element(BasePage.ABOUTUS)
        self.click_element(BasePage.ABOUT_SPUR)

    def how_it_work(self):
        self.hover_element(BasePage.ABOUTUS)
        self.click_element(BasePage.HOWITWORK)

    def privacy_policy(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_on_hidden_element(self.privacy)

    def terms_and_conditions(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_on_hidden_element(self.terms)

    def contactus(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        iframe = "designstudio-iframe"
        email = (By.XPATH, "//input[@id='offline-email']")
        message = (By.XPATH, "//textarea[@id='offline-description']")
        submit = (By.XPATH, "//input[@id='offline-send-email']")
        self.click_on_hidden_element(self.contactemail)
        self.driver.switch_to.frame(iframe)
        self.send_keys(email, "autotest@yopmail.com")
        self.send_keys(message, "Test message description")
        self.click_element(submit)

    def faq(self):
        time.sleep(2)
        self.click_on_hidden_element(self.FAQs)

    def find_couples(self, couplename):
        time.sleep(2)
        self.click_on_hidden_element(self.find_couple)
        self.clear_text_box(self.searchinput)
        self.send_keys(self.searchinput, couplename)

    def wedding_registry(self):
        self.hover_element(BasePage.Wedding_registry)
        self.click_element(BasePage.weddingregistry)

    def blogs(self):
        self.hover_element(BasePage.ABOUTUS)
        self.click_element(BasePage.BLOGS)
