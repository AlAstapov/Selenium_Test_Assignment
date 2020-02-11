from seleniumUi.pages.locators.main_page_locators import MainPageLocators
from seleniumUi.pages.base_page import BasePage, time_out_sec
from business import config


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_home_form_holder_start_testing_now_button(self, time_out=time_out_sec):
        self._click(MainPageLocators.HOME_FORM_HOLDER_START_TESTING_NOW_BUTTON_SELECTOR, time_out)

    def navigate(self):
        self._navigate(config.urls['main_page'])
