from selenium.webdriver import ActionChains

from Pages.BasePage import BasePage


class GuestView(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def guest_view(self):
        self.click_element(BasePage.Click_Home)
        self.send_keys(BasePage.Search_Box, 'Test Exp 123')
        self.click_element(BasePage.Click_Search)
        Hover = ActionChains(self.driver)
        Hover.move_to_element(BasePage.Hover_Image).perform()
        self.click_element(BasePage.Add_To_Registry)
