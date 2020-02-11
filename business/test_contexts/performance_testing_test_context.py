from seleniumUi.pages.performance_testing_tab import PerformanceTestingTab, time_out_sec


class PerformanceTestingTestContext:
    def __init__(self, driver):
        self.performance_testing_tab = PerformanceTestingTab(driver)

    def is_opened(self):
        return self.performance_testing_tab.is_opened(time_out=time_out_sec)

    def skip_wizard(self):
        self.performance_testing_tab.click_skip_wizard()
