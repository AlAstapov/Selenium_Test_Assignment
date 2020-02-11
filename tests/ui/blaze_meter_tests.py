import pytest
import unittest

from seleniumUi.drivers.browser import Browser
from business.Test_Contexts.main_page_test_context import MainPageTestContext
from business.Test_Contexts.registration_test_context import RegistrationTestContext
from business.Test_Contexts.performance_testing_test_context import PerformanceTestingTestContext
from business.Test_Contexts.unified_menu_test_context import UnifiedMenuTestContext
from business.Test_Contexts.EditAccountTestContext import EditAccountTestContext


class BlazeMeter(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser.get_chrome_driver()
        cls.main_page_test_context = MainPageTestContext(cls.driver)
        cls.main_page_test_context.navigate()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @pytest.mark.run(order=1)
    @pytest.mark.test_id(100000)
    def test_register_new_user(self):
        """Verifying start testing with new user"""
        # test contexts
        registration_window_test_context = RegistrationTestContext(self.driver)
        performance_testing_test_context = PerformanceTestingTestContext(self.driver)

        self.main_page_test_context.click_home_form_holder_start_testing_now_button()
        self.assertTrue(registration_window_test_context.is_opened(), "Registration window is not opened")

        registration_window_test_context.register_random_user()
        self.assertTrue(performance_testing_test_context.is_opened(), "Performance testing tab is not opened")

    @pytest.mark.test_id(100001)
    def test_edit_user_info(self):
        """Verifying editing user info"""
        # test contexts
        # user is logger in from test_register_new_user test
        unified_menu_test_context = UnifiedMenuTestContext(self.driver)
        edit_account_test_context = EditAccountTestContext(self.driver)

        unified_menu_test_context.open_personal_settings()
        edit_account_test_context.edit_account("UpdateFirstName", "UpdateLastName")
        self.assertTrue(edit_account_test_context.is_success_alert_displayed(), "Account changes wasn't saved")