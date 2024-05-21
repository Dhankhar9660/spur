"""Author: Balkishan Dhankhar
    Date: 11/03/2022
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import imaplib
import email


class BasePage:
    # define our class constructor
    def __init__(self, driver):
        self.driver = driver

    """Common Locators to all Test Classes """

    HOME = (By.XPATH, "//img[@class='header-logo']")
    EMAIL = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='passwrd']")
    LOGIN_ICON = (By.XPATH, "//a[@class='nav-link ng-star-inserted']")
    LOGIN_BTN = (By.XPATH, "//input[@value='log in']")
    ABOUTUS = (By.XPATH, "(//a[text()='About'])[1]")
    Wedding_registry = (By.XPATH, "(//a[text()='wedding registry'])[1]")
    ABOUT_HEADING = (By.XPATH, "//div[@class='nexExp_heading']")
    ABOUT_SPUR = (By.XPATH, "(//a[text()='ABOUT SPUR'])")
    FAQ = (By.XPATH, "(//a[text()='FAQs'])")
    HOWITWORK = (By.XPATH, "(//a[text()='How registries work'])")
    weddingregistry = (By.XPATH, "(//a[text()='why register with SPUR'])")
    BLOGS = (By.XPATH, "(//a[text()='Blog'])[1]")
    LOGOUT = (By.XPATH, "(//a[@class='nav-link ng-star-inserted'])[1]")
    DASHBOARD = (By.XPATH, "(//li[@class='nav-item ng-star-inserted active'])[1]")
    ADDEXP = (By.XPATH, "(//ul[@class='navbar-nav ml-auto']//a)[2]")
    OURREGISTRY = (By.XPATH, "(//li[@class='nav-item']//a)[23]")
    EXPERIENCE = (By.XPATH, "(//div[@class='product-name']//h2)[2]")
    ADD_TO_REGISTRY = (By.XPATH, "//button[@class='themeBtn rounded-theme secondry-theme mb-2']")
    ADD_TO_CART = (By.XPATH, "//div[@class='ng-star-inserted']//button[@class='themeBtn rounded-theme mb-2 btn-gray']")
    CHECKOUT = (By.XPATH, "//div[@class='cartpopup_checkout_btn']")
    BUYFORME = (By.XPATH, "(//div[@class='blockRadio']//label)[1]")
    NEXT = (By.XPATH, "(//div[@class='inputSubmitBtn']//input)[2]")
    NEXT1 = (By.XPATH, "(//div[@class='inputSubmitBtn']//input)[1]")
    CCINPUT = (By.XPATH, "//input[@placeholder='Credit Card Number']")
    MONTH = (By.XPATH, "//select[@formcontrolname='expiry_month']")
    YEAR = (By.XPATH, "//select[@formcontrolname='expiry_year']")
    CVV = (By.XPATH, "//input[@formcontrolname='cvv']")
    PLACE_ORDER = (By.XPATH, "//input[@value='Place order']")
    ORDERCONFMESSAGE = (By.XPATH, "//div[@class='col-12']//h1")
    SEARCHBOXEXP = (By.XPATH, "//div[@class='primeAutocomplete homeAutoCompCountryParent homeSerachWidth']//input")
    SEARCHITEM = (By.XPATH, "//div[text()='Test live exp']")
    QTY = (By.XPATH, "//option[text() ='Select Quantity']//parent::select")
    person = (By.XPATH, "//option[text() ='2 People']")
    CALENDER = (By.XPATH, "//input[@placeholder='Select Date']")
    DATE = (By.XPATH, "(//div[@class='p-datepicker-calendar-container ng-tns-c85-60 ng-star-inserted']//td)[33]")
    TIMESLOT = (By.XPATH, "//div[@class='availDateSEl selectMar']//select")
    ADDNEWEXP = "(//div[@class='expericence_addView']//span)[2]"
    EXPNAMEINPUT = (By.XPATH, "//div[@class='form-group']//input")
    NEXT2 = "//button[@class='form-control submit-button']"
    SUMMERY = (By.XPATH, "//div[@class='form-group']//textarea")
    NEXT3 = "//input[@class='twobtns-accept']"
    DETAILS = (By.XPATH, "//div[@class='form-group']//div//textarea")
    INCLUDE = (By.XPATH, "(//div[@class='mb-2']//textarea)[1]")
    EXCLUDE = (By.XPATH, "(//div[@class='mb-2']//textarea)[2]")
    SEASION = (By.XPATH, "(//div[@class='mb-2']//input)[1]")
    DAYS = (By.XPATH, "(//div[@class='mb-2']//input)[2]")
    SAMEADD = (By.XPATH, "//div[@class='custom-checked add-provider-check']//span")
    PRICE = (By.XPATH, "(//div[@class='ex-pricing-input']//input)[1]")
    TEX = (By.XPATH, "(//div[@class='ex-pricing-input']//input)[2]")
    REDIO_NO = (By.XPATH, "(//div[@class='customradio_wrap']//label)[2]")
    SUBMIT = "//button[@class='form-control submit-button']"
    EXP_HEADING = (By.XPATH, "//h1[@class='main_heading mb-4']")
    EXP_cong_msg = (By.XPATH, "//p[@class='my-5']")
    Buy_AS_VOUCHER = (By.XPATH, "//button[text()='BUY AS A VOUCHER']")
    Cart_popup_close = (By.XPATH, "//div[@class='cartpopup_box']//i")

    exp_name = "Test Auto Exp 123"
    Details = "Check out the complete schedule and route details of the 12935 Mumbai Bandra T Surat Intercity Exp on " \
              "RailYatri."
    Include = "drink , food, hotel"
    Exclude = "Smokeing, fule"
    Seasion = "Offered May – October"
    Days = "Daily"
    Price = "200"
    Tex = "10"

    Summery = "This is only for testing"
    CC_Number = "4111111111111111"
    Month = "05"
    Year = "2025"
    cvv = "123"
    ticket = "test"
    Orderconf = "ORDER RECEIVED"
    TICKET = (By.XPATH, "(//a[text()='SPURTicketing'])[1]")
    TKTTYPE = (By.XPATH, "(//a[text()=' CONCERTS'])[1]")
    ticketnameinput = (By.XPATH, "//input[@placeholder='Search Event Name']")
    search_button = (By.XPATH, "//button[text()= 'search']")
    EVENT = (By.XPATH, "(//div[@class='eventInfo'])[1]//div//a")
    TICKETBUY = (By.XPATH, "(//div[@class='button_buy'])[2]//button")
    SELECTACCOUNT = (By.XPATH, "//div[@class='col-md-6 ng-star-inserted']")
    OURTICKET = (By.XPATH, "//h2//span")
    REZDYEXP = "SWIMMING"
    FRIENDS = (By.XPATH, "(//ul[@class='navbar-nav ml-auto']//li//a)[4]")
    FINDFRIENDS = (By.XPATH, "(//div[@class='vertical-links-left']//a)[4]")
    FRIENDREQUEST = (By.XPATH, "(//div[@class='couples_list_item_action']//a)[1]")
    FRIENDREQUESTCNSL = (By.XPATH, "(//span[@class='friend_action_btns'])[1]")

    LOGIN_EMAIL_VALIDATION = (By.XPATH, "(//div[@class='ng-star-inserted'])[1]")
    LOGIN_PASSWORD_VALIDATION = (By.XPATH, "(//div[@class='ng-star-inserted'])[2]")

    # --------------------------- login details for stage server-------------------
    # COUPLE_EMAIL = "coupleuser@yopmail.com"
    # INDIVIDUAL_EMAIL = "individualuser@yopmail.com"
    # EP_EMAIL = "testexperience@yopmail.com"
    # CHARITY_EMAIL = "testcharity@yopmail.com"
    # ZOLA_EMAIL = "zolauser@yopmail.com"
    # JOY_EMAIL = "joyuser@yopmail.com"
    # KNOT_EMAIL = "knotuser@yopmail.com"
    # AUTOMATION_PASSWORD = "System@123"

    # -----------------login details for live server---------------------
    COUPLE_EMAIL = "Testuser76@yopmail.com"
    COUPLE_USER_NAME = "Automatoin"
    INDIVIDUAL_EMAIL = "individualuser@yopmail.com"
    EP_EMAIL = "testexperience@yopmail.com"
    CHARITY_EMAIL = "testcharity@yopmail.com"
    ZOLA_EMAIL = "testzola@yopmail.com"
    JOY_EMAIL = "testjoy@yopmail.com"
    KNOT_EMAIL = "knotuser@yopmail.com"
    AUTOMATION_PASSWORD = "123123"

    # Login error message
    Email_error_message = "Please enter the username"
    Password_error_message = "Please enter the password."

    # - Xpaths for the update profile-

    Setting = (By.XPATH, "//a[text() = 'Settings']")
    First_Name = (By.XPATH, "//input[@name='first_name']")
    Last_Name = (By.XPATH, "//input[@name='last_name']")
    Phone_Number = (By.XPATH, "(//input[@id = 'phone'])[1]")
    Partner_First_Name = (By.XPATH, "//input[@name='partner_first_name']")
    Partner_Last_Name = (By.XPATH, "//input[@name='partner_last_name']")
    Partner_Email = (By.XPATH, "//input[@name='partner_email']")
    Wedding_Date = (By.XPATH, "//input[@name='wedding_date']")
    Greetings = (By.XPATH, "//textarea[@name = 'greeting_text']")
    Couple_Hashtag = (By.XPATH, "//input[@name = 'couple_hashtag']")
    Home_Region = (By.XPATH, "//select[@name = 'homeRegion']")

    # Xpaths for the Honeymoon-

    Honeymoon = (By.XPATH, "(//a[@rel = 'tab11'])[1]")
    Honymoon_Location = (By.XPATH, "//input[@placeholder = 'Enter a location']")
    Mobile_Number = (By.XPATH, "(//input[@id= 'phone'])[2]")
    Trip_Start_Date = (By.XPATH, "//input[@formcontrolname = 'honeymoon_start_time']")
    Trip_End_Date = (By.XPATH, "//input[@formcontrolname = 'honeymoon_end_time']")

    Hotel_Loding = (By.XPATH, "//textarea[@name = 'honeymoon_hotel_lodge']")
    Update = "(//input[@value = 'Update'])[1]"

    # Xpaths for the update shipping
    Shipping = (By.XPATH, "(//a[text() = 'Shipping'])[1]")
    FirstName = (By.XPATH, "//input[@name = 'shipping_first_name']")
    LastName = (By.XPATH, "//input[@name = 'shipping_last_name']")
    Address = (By.XPATH, "//input[@name = 'shipping_address_1']")
    Country = (By.XPATH, "//span[@class = 'select2-selection__rendered']")
    Search_Country = (By.XPATH, "//input[@type = 'search']")
    Click_Update = "(//input[@value = 'Update'])[2]"

    # Xpaths for the invite partner
    Invite = (By.XPATH, "(//a[text() = 'INVITE PARTNER'])[1]")
    Revoke_Email = (By.XPATH, "//input[@value = 'REVOKE']")
    Email_Invitation = (By.XPATH, "//input[@name = 'email_invitation']")
    Click_Invite = (By.XPATH, "//input[@name = 'invite_partner']")

    # Xpaths for change password
    Click_ChangePassword = "(//a[text() = 'CHANGE PASSWORD'])[1]"
    Old_Password = (By.XPATH, "//input[@name = 'old_password']")
    New_Password = (By.XPATH, "//input[@name = 'new_password']")
    Confirm_Password = (By.XPATH, "//input[@name = 'cnfrm_password']")
    Submit = (By.XPATH, "//input[@value = 'Change Password']")

    Old_Pas_Validation_1 = (By.XPATH, "//div[text() = 'Old Password is required']")
    Old_Pas_Validation_2 = (By.XPATH, "//div[text() = 'Your old password is incorrect']")
    New_Pas_Validation_1 = (By.XPATH, "//div[text() = 'New Password is required']")
    New_Pas_Validation_2 = (By.XPATH, "//div[text() = 'New Password length should be minimum 6.']")
    Confirm_Pas_Validation_1 = (By.XPATH, "//div[text() = 'Confirm Password is required']")
    Confirm_Pas_Validation_2 = (By.XPATH, "//div[text() = 'password and confirm password must match.']")
    Confirm_Pas_Validation_3 = (By.XPATH, "//div[text() = 'Confirm Password length should be minimum 6.']")
    Log_Out = (By.XPATH, "//a[text() = 'LOGOUT']")

    # Xpaths for copy and paste url
    View_Our_Url = (By.XPATH, " //a[text()= ' View Our url']")
    Copy_Url = (By.XPATH, " //a[text()= 'Copy URL']")

    # Xpaths for activate/deactivate account
    Click_Account = "(//a[text() = 'DEACTIVATE ACCOUNT'])[1]"
    Deactivate_Account = (By.XPATH, "//input[@value = 'Deactivate Account']")
    AccountInactive = (By.XPATH, "(//div[@class = 'ng-star-inserted'])[2]")
    Activate_Account = (By.XPATH, "//input[@value = 'Activate Account']")
    AccountInactiveMsg = 'Account Inactive – You have deactivated your account and it is no longer active. To ' \
                         'reactivate, please visit DEACTIVATE ACCOUNT.'

    # Xpaths for GuestView ----------
    Click_Home = (By.XPATH, "(//a[text() = 'Home'])[1]")
    Search_Box = (By.XPATH, "(//input[@role = 'searchbox'])[4]")
    Click_Search = "//button[@class = 'primeSeach prime_active']"
    Product_Name = (By.XPATH, "//h2//a")
    Click_On_Product = "//div[@class = 'product-image lazyloaded']"
    Add_To_Registry = "//a[text() = 'Add to Registry  ']"
    Click_MyDashboard = (By.XPATH, "(//a[text() = 'My Dashboard'])[1]")
    Close_Popup = (By.XPATH, "(//button[@aria-label = 'Close'])[12]")
    Search_Product = (By.XPATH, "//input[@role = 'combobox']")
    Search = (By.XPATH, "//div[@id = 'ej2_dropdownlist_0_popup']")
    Add_To_Cart = "(//a[text()= 'add to cart'])[1]"
    Click_On_Cart = (By.XPATH, "(//span[@class = 'topcart-icon'])[2]")
    Product = (By.XPATH, "//div[@class = 'productName']")
    Remove_From_Cart = (By.XPATH, "//div[@class = 'productRemove']//a")
    Click_Yes_Button = (By.XPATH, "//a[text() ='Yes']")

    Remove_From_Registry = "//a[text() = 'Remove from Registry ']"

    # Define all common methods here, please comment as required for new methods

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title

    def refresh_page(self, driver):
        driver.refresh()

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def hover_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_element(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text_box(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
            Keys.CONTROL + 'a' + Keys.BACKSPACE)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_value(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).get_attribute(
            "value")
        return element

    def get_element_placeholder(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).get_attribute(
            "placeholder")
        return element

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def wait_for_invisibility_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def if_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(by_locator))
        return element

    def is_non_editable(self, by_locator):
        flag = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).is_enabled()
        return flag

    def is_selectedtrue(self):
        element = self.driver.find_element_by_id('checkbox-category-ef74cce8-db0b-461e-aabf-f69143661b31').is_selected()
        return element

    def get_list_of_elements(self, by_locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(by_locator))

    def click_on_hidden_element(self, locetor):
        element = self.driver.find_element(By.XPATH, locetor)
        self.driver.execute_script("arguments[0].click();", element)
        return element

    def click_on_hidden_element_by_selector(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        return element

    def get_otp_from_email(self, youremail, password, imap_server, otp_subject):
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(youremail, password)

        mail.select()
        mail.select("Inbox")

        result, data = mail.search(None, f'(SUBJECT "{otp_subject}")')

        latest_email_id = data[0].split()[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        otp = None
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    otp = part.get_payload()
                    break
        else:
            otp = email_message.get_payload()

        return otp
