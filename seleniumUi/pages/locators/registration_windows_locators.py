from selenium.webdriver.common.by import By


class RegistrationWindowLocators(object):
    FIRST_NAME_SELECTOR = (By.ID, "firstName")
    LAST_NAME_SELECTOR = (By.ID, "lastName")
    EMAIL_SELECTOR = (By.ID, "email")
    COMPANY_SELECTOR = (By.ID, "user.attributes.company")
    REGISTER_BUTTON_SELECTOR = (By.XPATH, ".//input[@value='Register']")
