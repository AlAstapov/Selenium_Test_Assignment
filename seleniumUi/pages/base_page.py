from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time_out_sec = 10


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _click(self, by_locator):
        WebDriverWait(self.driver, time_out_sec).until(EC.visibility_of_element_located(by_locator)).click()

    def _navigate(self, url):
        self.driver.get(url)

    def _clear_and_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, time_out_sec).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def _is_opened(self, by_locator):
        try:
            WebDriverWait(self.driver, time_out_sec).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            return False

        return True
