import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import smtplib
import imaplib
import email
from bs4 import BeautifulSoup

LOST_PASS = (By.XPATH, "//a[@class = 'frgpass']")
EMAILXPATH = (By.XPATH, "//input[@id='username']")
SUBMIT_REQUEST = (By.XPATH, "//input[@value='Submit Request']")
INPUT_OTP = (By.XPATH, "(//ng-otp-input[@id='otp']//input)[1]")
PASSWORD_INPUT = (By.XPATH, "//input[@id='new_password']")
CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='confirm_password']")
RESET_PASSWORD_BTN = (By.XPATH, "//input[@value='Reset Password']")

subject = "Forgot Password"
imap_server = "imap.gmail.com"


class Forgot_password(BasePage):

    def __init__(self, driver):
        # use super class of BasePage to get access to all the methods defined in BasePage
        super().__init__(driver)

    def forgot_password(self, emailid, apppassword, newpassword):
        self.click_element(BasePage.LOGIN_ICON)
        time.sleep(3)
        self.click_element(LOST_PASS)
        self.send_keys(EMAILXPATH, emailid)
        self.click_element(SUBMIT_REQUEST)
        time.sleep(3)
        otp = self.get_otp_from_email(emailid, apppassword, imap_server, subject)

        html_code = otp

        soup = BeautifulSoup(html_code, 'html.parser')

        otp_element = soup.find('span', {'name': '3D"codenumber"'})
        otp = otp_element.text if otp_element else None
        self.send_keys(INPUT_OTP, otp)
        self.send_keys(PASSWORD_INPUT, newpassword)
        self.send_keys(CONFIRM_PASSWORD_INPUT, newpassword)

        self.click_element(RESET_PASSWORD_BTN)
