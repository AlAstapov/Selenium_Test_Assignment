from seleniumUi.pages.locators.registration_windows_locators import RegistrationWindowLocators
from seleniumUi.pages.base_page import BasePage, time_out_sec


class RegistrationWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self, time_out=time_out_sec):
        return self._is_opened(RegistrationWindowLocators.REGISTER_BUTTON_SELECTOR, time_out)

    def clear_and_fill_first_name(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(RegistrationWindowLocators.FIRST_NAME_SELECTOR, text, time_out)

    def clear_and_fill_last_name(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(RegistrationWindowLocators.LAST_NAME_SELECTOR, text, time_out)

    def clear_and_fill_email(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(RegistrationWindowLocators.EMAIL_SELECTOR, text, time_out)

    def clear_and_fill_company(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(RegistrationWindowLocators.COMPANY_SELECTOR, text, time_out)

    def click_register(self, time_out=time_out_sec):
        self._click(RegistrationWindowLocators.REGISTER_BUTTON_SELECTOR, time_out)
