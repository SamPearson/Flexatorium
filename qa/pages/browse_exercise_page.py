from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BrowseExercisePage(BasePage):
    _exercise_list = {"by": By.ID, "value": "browse-exercise-list"}
    _exercise_card = {"by": By.CLASS_NAME, "value": "exercise-card"}
    _exercise_name = {"by": By.CLASS_NAME, "value": "exercise-name"}
    _exercise_description = {"by": By.CLASS_NAME, "value": "exercise-description"}
    _exercise_config_option_tag = {"by": By.CLASS_NAME, "value": "exercise-config-option-tag"}
    _delete_exercise_button = {"by": By.CLASS_NAME, "value": "delete-exercise-button"}

    def __init__(self, driver):
        self.driver = driver
        self.login()
        self._visit("/exercises/browse")
        assert self._is_displayed(self._exercise_list)

    def get_exercise_data(self):
        cards = self._find_all(self._exercise_card)
        if not cards:
            return False

        exercises = []

        for card in cards:
            exercises.append({
                "name": self._find_child(card, self._exercise_name).text,
                "description": self._find_child(card, self._exercise_description).text,
                "options": [c.text for c in self._find_children(card, self._exercise_config_option_tag)]
            })
            print(card)

        print(exercises)
        return exercises

    def get_exercise(self, name):
        for exercise in self.get_exercise_data():
            if name == exercise['name']:
                return exercise

        return False

    def get_exercise_card_element(self, name):
        for exercise in self._find_all(self._exercise_card):
            if name == self._find_child(exercise, self._exercise_name).text:
                return exercise

        return False

    def delete_exercise(self, name):
        exercise = self.get_exercise_card_element(name)

        delete_button = self._find_child(exercise, self._delete_exercise_button)
        delete_button.click()
