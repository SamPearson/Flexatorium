from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        try:
            return self._find_all(locator)[0]
        except IndexError:
            return False

    def _find_child(self, parent, locator):
        children = parent.find_elements(locator["by"], locator["value"])
        try:
            return children[0]
        except IndexError:
            return False

    def _find_children(self, parent, locator):
        children = parent.find_elements(locator["by"], locator["value"])
        try:
            return children
        except IndexError:
            return False

    def _find_all(self, locator):
        try:
            return self.driver.find_elements(locator["by"], locator["value"])
        except NoSuchElementException:
            return False

    def _click(self, locator):
        element = self._find(locator)
        assert element, f"Click action failed, cannot locate an element with {locator}"
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            e = self._find(locator)
            if e:
                return e.is_displayed()
            else:
                return False

    _success_message = {"by": By.ID, "value": "success-notif"}
    _failure_message = {"by": By.ID, "value": "failure-notif"}

    def success_message_present(self):
        return self._is_displayed(self._success_message, 1)

    def failure_message_present(self):
        return self._is_displayed(self._failure_message, 1)

    def failure_message_text(self):
        if self.failure_message_present():
            return self._find(self._failure_message).text
        else:
            return "No error message found"

    # Most tests will require logging in, so login page elements are stored here instead of
    # an independent page
    _login_page_email_input = {"by": By.CLASS_NAME, "value": "email-field"}
    _login_page_password_input = {"by": By.CLASS_NAME, "value": "password-field"}
    _login_page_submit_button = {"by": By.CLASS_NAME, "value": "submit-button"}

    # TODO: Do not hardcode credentials here
    def attempt_login(self, email="testuser@example.com", password="testuser_bestuser"):
        # Allows for failed login attempts without throwing exceptions
        # useful for testing error messages
        self._visit("/login")
        self._type(self._login_page_email_input, email)
        self._type(self._login_page_password_input, password)
        self._click(self._login_page_submit_button)

    def login(self, email="testuser@example.com", password="testuser_bestuser"):
        self.attempt_login(email, password)
        assert self.success_message_present(), f"Could not log in as {email} - {self.failure_message_text()}"

