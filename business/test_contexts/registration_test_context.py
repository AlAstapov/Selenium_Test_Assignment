from seleniumUi.pages.registration_window import RegistrationWindow
from utilities.random_util import generate_random_str
from business.items.user_registration_item import UserRegistrationItem


class RegistrationTestContext:
    def __init__(self, driver):
        self.registration_window = RegistrationWindow(driver)

    def register_user(self, user_registration_item):
        self.registration_window.clear_and_fill_first_name(user_registration_item.first_name)
        self.registration_window.clear_and_fill_last_name(user_registration_item.last_name)
        self.registration_window.clear_and_fill_email(user_registration_item.email)
        self.registration_window.clear_and_fill_company(user_registration_item.company)
        self.registration_window.click_register()

    def register_random_user(self):
        random_part = generate_random_str()
        user = UserRegistrationItem(f"{random_part}FirstName", f"{random_part}LastName",
                                    f"{random_part}@mai.ru", f"{random_part}Company")

        self.register_user(user)

    def is_opened(self):
        return self.registration_window.is_opened()