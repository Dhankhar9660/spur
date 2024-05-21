import time
import requests
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
from Pages.BasePage import BasePage
from Pages.Booking import Booking
from Pages.Search_experiences import SearchExp
from datetime import datetime


class TestBookingDate(BaseTest):
    url = "https://node.spurexperiences.com/v6/experience/get-calendar-dates-instant"
    people_select = (By.ID, "select_people")
    book_now_top = "//a[text() = 'Book Now']"
    people_option = (By.XPATH, "//select[@id='select_people']//option[3]")
    date_input = "//input[@id='ngbDate']"

    def test_get_available_dates(self):
        self.search = SearchExp(self.driver)
        self.search.exp_details_from_home_page("Seattle Dinner Cruise")
        time.sleep(5)
        url = self.driver.current_url
        slug = url.split('/')[-1]
        current_month = datetime.now().month
        current_year = datetime.now().year
        people_count = 2
        all_available_dates = []
        for i in range(3):
            month = current_month + i
            year = current_year + (month - 1) // 12  # Adjust year if month exceeds 12
            month = (month - 1) % 12 + 1  # Adjust month if it exceeds 12
            payload = {
                "month": month,
                "people_count": people_count,
                "slug": slug,
                "year": year
            }
            available_date = [Booking.get_available_dates(self.url, payload)]
            all_available_dates.extend(available_date)
        date_list = [date for sublist in all_available_dates for date in sublist]

        active_day = date_list[0]
        day = active_day.split('-')[-1]

        clickday = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"

        if len(date_list) > 0:
            self.search.click_on_hidden_element(self.book_now_top)
            time.sleep(3)
            self.search.click_element(self.people_select)
            time.sleep(2)
            self.search.click_element(self.people_option)
            self.search.click_on_hidden_element(self.date_input)
            time.sleep(5)
            self.search.click_on_hidden_element(clickday)
            time.sleep(4)
        else:
            print("Availability not available on this experience")
