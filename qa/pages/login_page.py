from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login-form"}
    _email_input = {"by": By.CLASS_NAME, "value": "email-field"}
    _password_input = {"by": By.CLASS_NAME, "value": "password-field"}
    _submit_button = {"by": By.CLASS_NAME, "value": "submit-button"}

    _success_message = {"by": By.ID, "value": "success-notif"}
    _failure_message = {"by": By.ID, "value": "failure-notif"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/login")
        assert self._is_displayed(self._login_form)

    def send_credentials(self, email, password):
        self._type(self._email_input, email)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def success_message_present(self):
        return self._is_displayed(self._success_message, 1)

    def failure_message_present(self):
        return self._is_displayed(self._failure_message, 1)
