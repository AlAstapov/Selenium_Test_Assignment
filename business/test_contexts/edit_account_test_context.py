from seleniumUi.pages.edit_account_page import EditAccountPage


class EditAccountTestContext:
    def __init__(self, driver):
        self.edit_account_page = EditAccountPage(driver)

    def edit_account(self, first_name, last_name):
        self.edit_account_page.clear_and_fill_first_name(first_name)
        self.edit_account_page.clear_and_fill_last_name(last_name)
        self.edit_account_page.save()

    def is_success_alert_displayed(self):
        return self.edit_account_page.is_success_alert_visible()
