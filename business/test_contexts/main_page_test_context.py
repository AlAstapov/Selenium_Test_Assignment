from seleniumUi.pages.main_page import MainPage


class MainPageTestContext:
    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def click_home_form_holder_start_testing_now_button(self):
        self.main_page.click_home_form_holder_start_testing_now_button()

    def navigate(self):
        self.main_page.navigate()
