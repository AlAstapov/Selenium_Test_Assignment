from seleniumUi.pages.locators.performance_testing_tab_locators import PerformanceTestingTabLocators
from seleniumUi.pages.base_page import BasePage, time_out_sec


class PerformanceTestingTab(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self, time_out=time_out_sec):
        return self._is_opened(PerformanceTestingTabLocators.URL_INPUT_SELECTOR, time_out)

    def fill_url(self, url, time_out=time_out_sec):
        self._clear_and_send_keys(PerformanceTestingTabLocators.URL_INPUT_SELECTOR, url, time_out)

    def click_skip_wizard(self, time_out=time_out_sec):
        self._click(PerformanceTestingTabLocators.SKIP_WIZARD_BUTTON_SELECTOR, time_out)
