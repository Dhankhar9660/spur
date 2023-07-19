import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(3)

nw = datetime.now()

dt = nw.strftime("%d%m%Y%H%M%S")
email = "soniya" + dt + "@yopmail.com"

# driver.find_element_by_xpath("(//div//child::a[@class='gb_d'])[1]").click()
# driver.find_element_by_xpath('(//div[@class="header__aside__buttons"]//a)[2]').click()
time.sleep(3)
Register = (By.XPATH,)
driver.find_element(By.XPATH, '//a[@class="ico-register"]').click()
# driver.find_element_by_xpath('(//label[@class="forcheckbox"])[2]')
driver.find_element_by_xpath('//input[@id="gender-female"]').click()
time.sleep(1)
driver.find_element_by_xpath('//input[@name="FirstName"]').send_keys("Sonu")
time.sleep(1)
driver.find_element_by_xpath('//input[@id="LastName"]').send_keys("Kumari")
time.sleep(1)
driver.find_element_by_xpath('//input[@name="Email"]').send_keys(email)
time.sleep(1)
driver.find_element_by_xpath('//input[@name="Password"]').send_keys("Soniya@123")
time.sleep(1)
driver.find_element_by_xpath('//input[@name="ConfirmPassword"]').send_keys("Soniya@123", Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//input[@class="button-1 register-continue-button"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@class="ico-logout"]').click()
time.sleep(1)
driver.find_element_by_xpath('//a[@class="ico-login"]').click()
time.sleep(2)
driver.find_element_by_xpath('//input[@name="Email"]').send_keys(email)
time.sleep(2)
driver.find_element_by_xpath('//input[@name="Password"]').send_keys("Soniya@123", Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//a[@class="ico-logout"]').click()
time.sleep(5)
# driver.find_element_by_xpath('//input[@name="pass"]').send_keys("System@123", Keys.ENTER)
# s = driver.find_element_by_xpath('(//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"])[1]').text
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
