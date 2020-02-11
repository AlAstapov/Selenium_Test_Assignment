from seleniumUi.pages.unified_menu import UnifiedMenu


class UnifiedMenuTestContext:
    def __init__(self, driver):
        self.unified_menu = UnifiedMenu(driver)

    def open_personal_settings(self):
        self.unified_menu.click_user_settings()
        self.unified_menu.click_user_personal_settings()
