from selenium.webdriver.common.by import By


class PerformanceTestingTabLocators(object):
    URL_INPUT_SELECTOR = (By.CLASS_NAME, "url-box")
    START_THE_TEST_BUTTON_SELECTOR = (By.CLASS_NAME, "btn-start-test")
    SKIP_WIZARD_BUTTON_SELECTOR = (By.CLASS_NAME, "skip")
