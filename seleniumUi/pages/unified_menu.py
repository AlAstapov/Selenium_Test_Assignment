from seleniumUi.pages.base_page import BasePage
from seleniumUi.pages.locators.unified_menu_locators import UnifiedMenuLocators


class UnifiedMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_user_settings(self):
        self._click_shadow_root_element(UnifiedMenuLocators.HEADER_LOCATOR[1], UnifiedMenuLocators.USER_SETTINGS[1])

    def click_user_personal_settings(self):
        # Should be clicked after 'click user settings' method
        self._click_shadow_root_element(UnifiedMenuLocators.HEADER_LOCATOR[1], UnifiedMenuLocators.USER_PERSONAL_SETTINGS[1])
