import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://spurexperiences.com/registries/BalSonu")
driver.implicitly_wait(15)
driver.find_element(By.XPATH, " //input[@placeholder='Find by Name/Category']").send_keys("test")
time.sleep(6)
# driver.switch_to.frame()
result = driver.find_elements(By.XPATH, "//div[@id = 'ej2_dropdownlist_0_popup']")
print(result)
new = []
for name in result:
    new = name.text
print(new)

# ABOUTUS = (By.XPATH, "(//a[text()='About'])[1]")
#
# about_element = driver.find_element(By.XPATH, "(//a[text()='About'])[1]")
# action = ActionChains(driver)
# action.move_to_element(about_element).perform()

time.sleep(8)

# Get the text from the clipboard
clipboard_text = pyperclip.paste()

# Print the clipboard text
print("Clipboard text:", clipboard_text)
