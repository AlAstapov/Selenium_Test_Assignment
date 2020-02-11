from selenium.webdriver.common.by import By


class EditAccountLocators(object):
    FIRST_NAME_SELECTOR = (By.ID, 'firstName')
    LAST_NAME_SELECTOR = (By.ID, 'lastName')
    SAVE_BUTTON_SELECTOR = (By.XPATH, ".//button[@value='Save']")
    SUCCESS_ALERT_SELECTOR = (By.CLASS_NAME, "alert-success")
