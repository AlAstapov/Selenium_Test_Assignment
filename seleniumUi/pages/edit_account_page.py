from seleniumUi.pages.locators.edit_account_locators import EditAccountLocators
from seleniumUi.pages.base_page import BasePage, time_out_sec


class EditAccountPage (BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def clear_and_fill_first_name(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(EditAccountLocators.FIRST_NAME_SELECTOR, text, time_out)

    def clear_and_fill_last_name(self, text, time_out=time_out_sec):
        self._clear_and_send_keys(EditAccountLocators.LAST_NAME_SELECTOR, text, time_out)
        
    def save(self, time_out=time_out_sec):
        self._click(EditAccountLocators.SAVE_BUTTON_SELECTOR, time_out)

    def is_success_alert_visible(self, time_out=time_out_sec):
        return self._is_element_visible(EditAccountLocators.SUCCESS_ALERT_SELECTOR, time_out)
