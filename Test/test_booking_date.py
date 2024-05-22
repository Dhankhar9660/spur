import time

from selenium.common import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from Test.test_Base import BaseTest
from Pages.Booking import Booking
from Pages.Search_experiences import SearchExp
from datetime import datetime


class TestBookingDate(BaseTest):
    url = "https://node.spurexperiences.com/v6/experience/get-calendar-dates-instant"
    people_select = (By.ID, "select_people")
    book_now_top = "//a[text() = 'Book Now']"
    people_option = (By.XPATH, "//select[@id='select_people']//option[3]")
    date_input = "//input[@id='ngbDate']"
    next_month = "//button[@aria-label='Next month']"

    def test_get_available_dates(self):
        try:
            self.search = SearchExp(self.driver)
            self.search.exp_details_from_home_page("Seattle Dinner Cruise")
            time.sleep(5)
            url = self.driver.current_url
            slug = url.split('/')[-1]
            current_month = datetime.now().month
            current_year = datetime.now().year
            people_count = 2
            all_available_dates = {}
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
                available_dates = [Booking.get_available_dates(self.url, payload)]
                all_available_dates[f'month_{i + 1}'] = available_dates

            month_1_dates = all_available_dates['month_1'][0]
            month_2_dates = all_available_dates['month_2'][0]
            month_3_dates = all_available_dates['month_3'][0]

            if len(month_1_dates) > 0:
                if len(month_1_dates) > 1:
                    active_date = month_1_dates[1]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                else:
                    active_date = month_1_dates[0]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                self.search.click_on_hidden_element(self.book_now_top)
                time.sleep(3)
                self.search.click_element(self.people_select)
                time.sleep(2)
                self.search.click_element(self.people_option)
                self.search.click_on_hidden_element(self.date_input)
                time.sleep(5)
                self.search.click_on_hidden_element(active_day)
                time.sleep(4)

            elif len(month_2_dates) > 0:
                if len(month_1_dates) > 1:
                    active_date = month_1_dates[1]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                else:
                    active_date = month_1_dates[0]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                self.search.click_on_hidden_element(self.book_now_top)
                time.sleep(3)
                self.search.click_element(self.people_select)
                time.sleep(2)
                self.search.click_element(self.people_option)
                self.search.click_on_hidden_element(self.date_input)
                time.sleep(5)
                self.search.click_on_hidden_element(self.next_month)
                time.sleep(5)
                self.search.click_on_hidden_element(active_day)
                time.sleep(4)

            elif len(month_3_dates) > 0:
                if len(month_1_dates) > 1:
                    active_date = month_1_dates[1]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                else:
                    active_date = month_1_dates[0]
                    date = datetime.strptime(active_date, "%Y-%m-%d")
                    day = date.day
                    active_day = f"//span[@class='custom-day disabled-date ng-star-inserted' and text() =' {day} ']"
                    print(active_day)
                self.search.click_on_hidden_element(self.book_now_top)
                time.sleep(3)
                self.search.click_element(self.people_select)
                time.sleep(2)
                self.search.click_element(self.people_option)
                self.search.click_on_hidden_element(self.date_input)
                time.sleep(5)
                self.search.click_on_hidden_element(self.next_month)
                time.sleep(5)
                self.search.click_on_hidden_element(self.next_month)
                time.sleep(5)
                self.search.click_on_hidden_element(active_day)
                time.sleep(4)
            else:
                print("Availability not available on this experience for next 3 months")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout occurred: {e}")
        except WebDriverException as e:
            print(f"WebDriver exception occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
