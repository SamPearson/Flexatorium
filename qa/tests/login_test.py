import pytest
from pages import login_page


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login(self, driver):
        return login_page.LoginPage(driver)

    @pytest.mark.smoke
    def test_valid_credentials(self, login):
        login.send_credentials("bill@partycentral.net", "sillybilly")
        assert login.success_message_present(), "Could not log in - was the hard-coded test user registered?"

    @pytest.mark.midweight
    def test_invalid_credentials(self, login):
        login.send_credentials("bademail@addr.ess", "badpassword")
        assert login.failure_message_present()
