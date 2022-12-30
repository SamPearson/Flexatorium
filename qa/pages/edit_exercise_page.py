from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EditExercisePage(BasePage):
    _edit_exercise_form = {"by": By.ID, "value": "edit-exercise-form"}

    _exercise_name_field = {"by": By.CLASS_NAME, "value": "name-field"}
    _exercise_description_field = {"by": By.CLASS_NAME, "value": "description-field"}

    _config_option_table = {"by": By.CLASS_NAME, "value": "config-option-fields"}
    _config_option_row = {"by": By.CLASS_NAME, "value": "config-option-row"}

    _config_option_type = {"by": By.CLASS_NAME, "value": "config-type-field"}
    _config_option_unit = {"by": By.CLASS_NAME, "value": "config-unit-field"}
    _add_config_option_button = {"by": By.CLASS_NAME, "value": "add-config-option-button"}
    _delete_config_option_button = {"by": By.CLASS_NAME, "value": "delete-config-option-button"}
    _save_button = {"by": By.ID, "value": "save-button"}

    def __init__(self, driver):
        self.driver = driver
        self.login()
        self._visit("/exercises/edit")
        assert self._is_displayed(self._edit_exercise_form)

    def fill_form(self, name, description, config_options):
        self._type(self._exercise_name_field, name)
        self._type(self._exercise_description_field, description)

        while len(config_options) > len(self._find_all(self._config_option_unit)):
            self._click(self._add_config_option_button)

        # config_options will be sent as a tuple of intended values.
        # these values need to be unzipped and then re-zipped with the fields they're targetting
        unzipped = list(zip(*config_options))
        types = zip(unzipped[0], self._find_all(self._config_option_type))
        for config_type, config_type_field in types:
            config_type_field.send_keys(config_type)

        units = zip(unzipped[1], self._find_all(self._config_option_unit))
        for config_unit, config_unit_field in units:
            config_unit_field.send_keys(config_unit)

    def delete_option(self, unit):
        matching_options = [option for option in self._find_all(self._config_option_row)
                            if self._find_child(option, self._config_option_unit) == unit]

        assert len(matching_options), f'Cannot delete option "{unit}", could not find matching option'
        assert len(matching_options) == 1, f'Cannot delete option - too many options matching "{unit}"'

        delete_button = self._find_child(matching_options[0], self._delete_config_option_button)
        delete_button.click()
