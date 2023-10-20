import os
import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Cms import CmsPage


class TestCmsPage(BaseTest):
    policy = (By.XPATH, "//h2[@class='termsHeading']")
    results = (By.XPATH, "//div[@class='wsa_list_head']")
    nodata = (By.XPATH, "//div[text() = 'No Record Found']")

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.about
    def test_about_us(self, request):

        self.cms = CmsPage(self.driver)
        self.cms.about()
        time.sleep(8)

        try:
            page_title = self.cms.get_element_text(BasePage.ABOUT_HEADING)
        except TimeoutException:
            print("About us Page title is not loading")
            raise

        try:
            assert page_title == "About Spur"

        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.howitwork
    def test_how_it_work(self, request):

        self.hit = CmsPage(self.driver)
        self.hit.how_it_work()
        time.sleep(8)
        try:
            page_title = self.hit.get_element_text(BasePage.ABOUT_HEADING)
        except TimeoutException:
            print("How It Works Page is not loading")
            raise
        try:
            assert page_title == "How It Works"
        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.policy
    def test_privacy_policy1(self, request):

        self.pp = CmsPage(self.driver)
        self.pp.privacy_policy()
        time.sleep(3)

        try:
            page_title = self.pp.get_element_text(self.policy)
        except TimeoutException:
            print("How It Works Page is not loading")
            raise
        try:
            assert page_title == "PRIVACY POLICY"
        except AssertionError:
            print("page title not matched")
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.terms
    def test_terms_condition(self, request):

        self.terms = CmsPage(self.driver)
        self.terms.terms_and_conditions()
        time.sleep(2)
        try:
            page_title = self.terms.get_element_text(self.policy)
        except TimeoutException:
            print("T&C page not loading.")
            raise
        try:
            assert page_title == "GENERAL TERMS & CONDITIONS"
        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.contact
    def test_contactus(self, request):
        thankyou = (By.XPATH, "//div[@class='message-text message-offline-confirm']")
        minimize = (By.XPATH, "//div[@id='icon-minimize']")
        self.contact = CmsPage(self.driver)
        self.contact.contactus()
        time.sleep(2)
        try:
            thank_you_message = self.contact.get_element_text(thankyou)
            self.contact.click_element(minimize)

            self.driver.switch_to.default_content()
        except TimeoutException:
            print("email popup not open")
            self.driver.switch_to.default_content()
            raise
        try:
            assert thank_you_message == "Thank you,\nYour message has been sent."
            self.driver.switch_to.default_content()
        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            self.driver.switch_to.default_content()

            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.faq
    def test_faq(self, request):
        page_title = (By.XPATH, "//h1[@class='faq_heading']")
        subhead = (By.XPATH, "//p[@class='faq_head_text']")
        faq_category_list = (By.XPATH, "//h2[@class='team-block-heading']")

        self.faq = CmsPage(self.driver)
        self.faq.faq()
        time.sleep(2)
        try:
            title = self.faq.get_element_text(page_title)
            subtitle = self.faq.get_element_text(subhead)
            category_list = self.faq.get_list_of_elements(faq_category_list)
        except TimeoutException:
            print("Faq page not loading")
            raise
        try:
            assert title == "FAQs"
            assert subtitle == "Please click below on what category of user you are to see frequently asked " \
                               "questions.\nIf you still don't have your answer, please email info@spurexperiences.com"

            category = []

            for i in category_list:
                category.append(i.text)
            assert category == ['Wedding Registry', 'Experience Gifting', 'Buy for Yourself', 'Experience Providers',
                                'Charity Partners', 'General Questions']

        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.findcouple
    def test_find_couple(self, request):
        self.couple = CmsPage(self.driver)
        self.couple.find_couples("Balkishan Dhankhar testpartner partner")
        name_result = []
        try:
            result_list = self.couple.get_list_of_elements(self.results)

            for i in result_list:
                name_result.append(i.text)
        except TimeoutException:
            print("Search result not coming")

        try:
            assert "BALKISHAN DHANKHAR & TESTPARTNER PARTNER" in name_result

        except AssertionError:
            # Create a unique timestamp for the screenshot
            timestamp = str(int(time.time()))

            # Get the current test name
            test_name = request.node.name
            # Create a unique file name using the test name and timestamp
            file_name = f"{test_name}_{timestamp}.png"

            # Specify the directory path to save the screenshot
            directory = "C:/Users/HP/PycharmProjects/spur-automations/Screenshot/"

            # Create the full path by joining the directory path and file name
            screenshot_path = os.path.join(directory, file_name)

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.wedding_registry
    def test_wedding_registry(self, request):
        self.couple = CmsPage(self.driver)
        self.couple.wedding_registry()
        time.sleep(3)
        try:
            image = (By.XPATH, "(//div[@class='row ng-star-inserted'])[1]")
            result = self.couple.is_visible(image)
            assert result, "Image not visible"
        except Exception as e:
            print(e, "Image not loading")
            raise
        try:
            heading = (By.XPATH, "//h2[text()= 'WHAT IS SPUR REGISTRY?']")
            result = self.couple.is_visible(heading)
            assert result == True
        except Exception as e:
            print(e, "heading not available ")
            raise
        try:
            image = (By.XPATH, "(//div[@class='row ng-star-inserted'])[1]")
            result = self.couple.is_visible(image)
            assert result == True
        except Exception as e:
            print(e, "image not loading")
            raise
        try:
            search_section = (By.XPATH, "(//div[@class='container'])[3]")
            result = self.couple.is_visible(search_section)
            assert result == True
        except Exception as e:
            print(e, "search section not loading")
            raise

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.Blogs
    def test_blogs(self, request):
        self.blog = CmsPage(self.driver)
        self.blog.blogs()
        time.sleep(1)
        try:
            image = (By.XPATH, "//img[@class='banner_mobile ls-is-cached lazyloaded']//parent::div")
            result = self.blog.is_visible(image)
            print(result)
            assert result, "Image not visible"
        except Exception as e:
            print(e, "Image not loading")
            raise
        try:
            heading = (By.XPATH, "//h1[text()='5 Wedding Traditions to Ditch (Volume #5)']")
            result = self.blog.is_visible(heading)
            assert result, "Heading not visible"
        except Exception as e:
            print(e, "heading not available ")

        try:
            artical = (By.XPATH, "//h2[text()='LATEST ARTICLES']")
            result = self.blog.is_visible(artical)
            assert result, "ARTICLES not visible"
        except Exception as e:
            print(e, "Article not available ")

        try:
            artical_by = (By.XPATH, "//h2[text()='SPUR ARTICLES BY CATEGORY']")
            result = self.blog.is_visible(artical_by)
            assert result, "ARTICLES not visible"
        except Exception as e:
            print(e, "Spur Article not available ")

    @pytest.mark.regression
    @pytest.mark.alltest
    @pytest.mark.Blogs
    def test_blogs_details(self, request):
        self.blog = CmsPage(self.driver)
        self.blog.blogs()
        time.sleep(2)
        details = "((//div[@class='card'])[1]//div)[1]//a"
        self.blog.click_on_hidden_element(details)
        time.sleep(2)
        try:
            image = (By.XPATH, "//div[@class='tkt_back ng-star-inserted']")
            result = self.blog.is_visible(image)
            assert result, "Image not visible"
        except Exception as e:
            print(e, "Image not loading")
            raise
        try:
            heading = (By.XPATH, "//h2[text()='Spur received four awards from The Knot.']")
            result = self.blog.is_visible(heading)
            assert result, "Heading not visible"
        except Exception as e:
            print(e, "heading not available ")
