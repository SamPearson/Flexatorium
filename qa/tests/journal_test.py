import pytest
from pages import journal_page
from .testing_utilities.mock_data_generation import random_string


@pytest.mark.journal
class TestJournal:
    @pytest.fixture
    def page(self, driver):
        return journal_page.JournalPage(driver)

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_add_note(self, page):
        note_text = random_string(10)
        page.add_note(note_text)

        assert page.success_message_present(), "Failed to add note, could not find success message"
        assert page.note_present(note_text), f'Could not find note with text "{note_text}"'

    @pytest.mark.midweight
    def test_empty_note(self, page):
        note_text = ""
        page.add_note(note_text)

        assert page.failure_message_present(), "Attempted to add empty note, did not see failure message"

    @pytest.mark.midweight
    @pytest.mark.dependency(depends=["test_add_note"])
    def test_delete_note(self, page):
        note_text = random_string(10)
        page.add_note(note_text)

        page.delete_note(note_text)
        assert not page.note_present(note_text), f'Failed to delete note "{note_text}", note still exists'