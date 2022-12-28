from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JournalPage(BasePage):
    _journal_table = {"by": By.ID, "value": "notes"}
    ''' "journal entry" and "note" are not interchangeable.
        They currently appear to be because only plain text notes can be entered into the journal.
        Eventually other things like completed workouts will also be journal entries.
        A note is strictly text only.'''
    _journal_entry = {"by": By.CLASS_NAME, "value": "journal-entry"}
    _note_text_input = {"by": By.CLASS_NAME, "value": "note-text-input"}
    _add_note_button = {"by": By.CLASS_NAME, "value": "add-note-button"}
    _delete_note_button = {"by": By.CLASS_NAME, "value": "delete-note-button"}

    def __init__(self, driver):
        self.driver = driver
        self.login()
        self._visit("/journal")
        assert self._is_displayed(self._journal_table)

    def add_note(self, text):
        self._type(self._note_text_input, text)
        self._click(self._add_note_button)

    def get_journal_entries(self):
        entries = self._find_all(self._journal_entry)
        if entries:
            return entries
        else:
            return False

    def note_present(self, text):
        for j in self.get_journal_entries():
            if text in j.text:
                return True

        return False

    def delete_note(self, text):
        matching_notes = [n for n in self.get_journal_entries() if text in n.text]
        assert len(matching_notes), f'Cannot delete note "{text}", could not find matching note'
        assert len(matching_notes) == 1, f'Cannot delete note - too many notes matching "{text}"'

        delete_button = self._find_child(matching_notes[0], self._delete_note_button)
        delete_button.click()

