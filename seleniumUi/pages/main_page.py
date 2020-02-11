from Selenium_Ui.Pages.Locators.main_page_locators import MainPageLocators
from Selenium_Ui.Pages.base_page import BasePage
from Tests import config


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_home_form_holder_start_testing_now_button(self):
        self._click(MainPageLocators.HOME_FORM_HOLDER_START_TESTING_NOW_BUTTON_SELECTOR)

    def navigate(self):
        self._navigate(config.urls['main_page'])
