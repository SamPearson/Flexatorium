import pytest
from pages import signup_page
from .testing_utilities.mock_data_generation import FlexatoriumUser

@pytest.mark.signup
class TestSignup:
    @pytest.fixture
    def page(self, driver):
        return signup_page.SignupPage(driver)

    @pytest.mark.smoke
    def test_account_registration(self, page):
        test_user = FlexatoriumUser()
        page.register(test_user.username, test_user.email, test_user.password)
        assert page.success_message_present()

    @pytest.mark.midweight
    def test_nonmatching_passwords(self, page):
        test_user = FlexatoriumUser()
        page.fill_registration_form(test_user.username, test_user.email, test_user.password, "nonmatching password")
        page._click(page._submit_button)

        assert page.password_error_present()
