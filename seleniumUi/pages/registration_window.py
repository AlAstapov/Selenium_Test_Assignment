from Selenium_Ui.Pages.Locators.registration_windows_locators import RegistrationWindowLocators
from Selenium_Ui.Pages.base_page import BasePage


class RegistrationWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self):
        return self._is_opened(RegistrationWindowLocators.REGISTER_BUTTON_SELECTOR)

    def fill_first_name(self, text):
        self._clear_and_send_keys(RegistrationWindowLocators.FIRST_NAME_SELECTOR, text)

    def fill_last_name(self, text):
        self._clear_and_send_keys(RegistrationWindowLocators.LAST_NAME_SELECTOR, text)

    def fill_email(self, text):
        self._clear_and_send_keys(RegistrationWindowLocators.EMAIL_SELECTOR, text)

    def fill_company(self, text):
        self._clear_and_send_keys(RegistrationWindowLocators.COMPANY_SELECTOR, text)

    def click_register(self):
        self._click(RegistrationWindowLocators.REGISTER_BUTTON_SELECTOR)