from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    _signup_form = {"by": By.ID, "value": "signup-form"}
    _username_input = {"by": By.CLASS_NAME, "value": "username-field"}
    _email_input = {"by": By.CLASS_NAME, "value": "email-field"}
    _password_input = {"by": By.CLASS_NAME, "value": "password-field"}
    _password_confirmation = {"by": By.CLASS_NAME, "value": "password-confirm-field"}
    _submit_button = {"by": By.CLASS_NAME, "value": "submit-button"}

    _username_error = {"by": By.CLASS_NAME, "value": "username-error"}
    _email_error = {"by": By.CLASS_NAME, "value": "email-error"}
    _password_error = {"by": By.CLASS_NAME, "value": "password-error"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/sign-up")
        assert self._is_displayed(self._signup_form)

    def fill_registration_form(self, username, email, password, password2):
        self._type(self._username_input, username)
        self._type(self._email_input, email)
        self._type(self._password_input, password)
        self._type(self._password_confirmation, password2)

    def register(self, username, email, password):
        self.fill_registration_form(username, email, password, password)
        self._click(self._submit_button)

    def password_error_present(self):
        return bool(self._find(self._password_error))

    def password_error(self):
        return self._find(self._password_error).get_text()
