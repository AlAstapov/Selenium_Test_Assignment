from selenium.webdriver.common.by import By


class UnifiedMenuLocators(object):
    HEADER_LOCATOR = (By.CSS_SELECTOR, "bzm-header")
    USER_SETTINGS = (By.CSS_SELECTOR, ".dropdown-toggle")
    USER_PERSONAL_SETTINGS = (By.CSS_SELECTOR, "a[href*='personal']")
