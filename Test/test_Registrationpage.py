""" Test Page for Login Checks
Author: Balkishan Dhankhar"""

import time
import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.RegistrationPage import Registration
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.loginsignup
class Test_Registration(BaseTest):

    def test_Registration(self):
        self.reg = Registration(self.driver)
        self.reg.Regist()
        time.sleep(5)
