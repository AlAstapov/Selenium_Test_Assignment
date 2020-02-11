from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from business import config

time_out_sec = config.time_out_sec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _click(self, by_locator, time_out=time_out_sec):
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(by_locator)).click()

    def _click_shadow_root_element(self, root_locator_value, element_locator_value):
        # use jss + css to click shadowRoot elements
        js_shadow_root_click = f"document.querySelector(\"{root_locator_value}\").shadowRoot.querySelector(\"{element_locator_value}\").click()"
        self.driver.execute_script(js_shadow_root_click)

    def _navigate(self, url):
        self.driver.get(url)

    def _clear_and_send_keys(self, by_locator, text, time_out=time_out_sec):
        element = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def _switch_to_frame(self, by_locator, time_out=time_out_sec):
        frame = WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(by_locator))
        self.driver.switch_to.frame(frame)

    def _is_element_visible(self, by_locator, time_out=time_out_sec):
        try:
            WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            return False

        return True

    def _is_opened(self, by_locator, time_out=time_out_sec):
        return self._is_element_visible(by_locator, time_out)
