import time
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Test.test_Base import BaseTest
import pandas as pd


class Test_SEO(BaseTest):

    def test_seocheck(self):
        ID = (By.XPATH, "//div[@id='center_col']")
        link = (By.XPATH, "//a")
        self.asd = LoginPage(self.driver)
        df = pd.read_excel('C:/Users/HP/PycharmProjects/Spurowebest/Test/test-excel.xlsx')

        urls = df['URL'].tolist()
        df['Indexing Status'] = ''
        for i, url_to_check in enumerate(urls):
            search_query = f'site:{url_to_check}'
            google_search_url = f'https://www.google.com/search?q={search_query}'
            self.asd.driver.get(google_search_url)
            time.sleep(8)

            # search_results = self.asd.get_list_of_elements(ID)
            search_results = self.asd.driver.find_elements(By.CSS_SELECTOR, 'div.g')

            is_indexed = False
            for result in search_results:

                link_element = result.find_element(By.CSS_SELECTOR, 'a')
                link_url = link_element.get_attribute('href')
                # print(link_url)
                # print(url_to_check)
                if url_to_check in link_url:
                    is_indexed = True
                    break

            if is_indexed:
                df.at[i, 'Indexing Status'] = 'Indexed'
            else:
                df.at[i, 'Indexing Status'] = 'Not Indexed'

        df.to_excel('C:/Users/HP/PycharmProjects/Spurowebest/Test/test-excel.xlsx', index=False)
