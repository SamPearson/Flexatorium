import pytest
from pages import base_page


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def page(self, driver):
        return base_page.BasePage(driver)

    @pytest.mark.smoke
    def test_valid_credentials(self, page):
        page.login()
        assert page.success_message_present()

    @pytest.mark.midweight
    def test_invalid_credentials(self, page):
        page.attempt_login("UnregisteredEmail@example.info", "L")
        assert page.failure_message_present()
