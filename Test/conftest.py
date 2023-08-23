import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from Config.config import TestData


# Pass params as "chrome", "edge", "firefox", "safari" depending on which browsers tests need to be run on

@pytest.fixture(params=["chrome"], scope="class")
def init_driver_here(request):
    """________________SETUP-----------------"""
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")

        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_extension("C:/Users/HP/Downloads/Nimbus-Screenshot---Screen-Video-Recorder.crx")

        # Pass the argument 1 to allow and 2 to block
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 3,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        })
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

    #     # Update for Mac based on the PATH or use web-driver manager
    # elif request.param == "edge":
    #     # Comment or Uncomment as required for running on Mac
    #     # desired_cap = {}
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    # elif request.param == "firefox":
    #     # Comment or Uncomment as required for running on Mac
    #     #   driver = webdriver.Firefox(executable_path='/Users/romabasnet/Downloads/geckodriver')
    #     # options = Options()
    #     # options.binary_location = r'C:\Users\RXB1002A\AppData\Local\Mozilla Firefox\firefox.exe'
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # elif request.param == "safari":
    #     driver = webdriver.Safari()
    else:
        print("Please enter right browser name" + request.param)
    request.cls.driver = driver

    driver.implicitly_wait(15)
    """driver.set_window_size(375, 820)
    driver.set_window_position(500, 0)"""
    driver.get(TestData.BASE_URL)
    # driver.get(TestData.PROD_LOGIN_URL)
    driver.implicitly_wait(20)

    yield
    """________________TEAR DOWN----------------"""
    driver.quit()
