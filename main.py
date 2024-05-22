import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
import re
from datetime import datetime

# import datetime

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("")

# driver.find_element(By.XPATH, " //input[@placeholder='Find by Name/Category']").send_keys("test")
# time.sleep(6)
# # driver.switch_to.frame()
# result = driver.find_elements(By.XPATH, "//div[@id = 'ej2_dropdownlist_0_popup']")
# print(result)
# new = []
# for name in result:
#     new = name.text
# print(new)

# ABOUTUS = (By.XPATH, "(//a[text()='About'])[1]")
#
# about_element = driver.find_element(By.XPATH, "(//a[text()='About'])[1]")
# action = ActionChains(driver)
# action.move_to_element(about_element).perform()
#
# time.sleep(8)
#
# # Get the text from the clipboard
# clipboard_text = pyperclip.paste()
#
# # Print the clipboard text
# print("Clipboard text:", clipboard_text)

# original_string = "This is an (dynamic wasdorld)"
# result_string = re.sub(r'\([^)]*\)', '', original_string).strip()
# print(result_string)


# EXP_Name = "test auto " + datetime.datetime.now().strftime("%H%M%S%B%d%Y")
# print(EXP_Name)
# ab = [3, 4, 55, 55]
# b = 553
# assert b in ab
# print("b  in list")
# now = datetime.now()
# today = "98899"
# print(type(today))
# str_value_without_zeros = today.lstrip('0')
# print(str_value_without_zeros)
# driver.switch_to.default_content()
#
# print(datetime.now().month)
# print(datetime.now().year)
# a = []
# b = [1, 2, 3, 4]
#



# c = ['2024-05-25', '2024-05-31']
# b = c[0]
# print(b)
# d = c[0]
# # d = d.split('-')[-1]
# # print(d)

# all_available_dates = {
#     'month_1': [['2024-05-31']],
#     'month_2': [['2024-06-01', '2024-06-06', '2024-06-13', '2024-06-14', '2024-06-15', '2024-06-20', '2024-06-22', '2024-06-27', '2024-06-28', '2024-06-29']],
#     'month_3': [['2024-07-05', '2024-07-06', '2024-07-11', '2024-07-12', '2024-07-13', '2024-07-18', '2024-07-19', '2024-07-20', '2024-07-25', '2024-07-27']]
# }
#
# # Extracting the lists from the dictionary
# month_1_dates = all_available_dates['month_1'][0]
# month_2_dates = all_available_dates['month_2'][0]
# month_3_dates = all_available_dates['month_3'][0]
#
# # Printing the results to verify
# print("Available dates for month 1:", month_1_dates)
# print("Available dates for month 2:", month_2_dates)
from datetime import datetime

# Given date string
date_string = "2024-05-25"

# Parse the date string into a datetime object
date_object = datetime.strptime(date_string, "%Y-%m-%d")

# Extract the day
day = date_object.day

# Print the day
print(day)