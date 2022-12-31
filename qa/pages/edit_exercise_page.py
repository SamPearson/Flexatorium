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
    _save_button = {"by": By.ID, "value": "save_button"}

    def __init__(self, driver, action):
        self.driver = driver
        self.login()
        if action == 'edit':
            self._visit("/exercises/edit")
        elif action == 'create':
            self._visit("/exercises/create")
        else:
            assert False, "edit exercise page object must be created with 'edit' or 'create' action"

        assert self._is_displayed(self._edit_exercise_form)

    def fill_form(self, name, description, config_options):
        self._type(self._exercise_name_field, name)
        self._type(self._exercise_description_field, description)

        while len(config_options) > len(self._find_all(self._config_option_unit)):
            self._click(self._add_config_option_button)

        if config_options:
            # config_options will be sent as a tuple of intended values.
            # these values need to be unzipped and then re-zipped with the fields they're targetting
            unzipped = list(zip(*config_options))
            types = zip(unzipped[0], self._find_all(self._config_option_type))
            for config_type, config_type_field in types:
                config_type_field.send_keys(config_type)

            units = zip(unzipped[1], self._find_all(self._config_option_unit))
            for config_unit, config_unit_field in units:
                config_unit_field.send_keys(config_unit)

    def create_exercise(self, name, description, config_options):
        self.fill_form(name, description, config_options)
        self._click(self._save_button)

    def config_option(self, unit):
        matching_options = [option for option in self._find_all(self._config_option_row)
                            if self._find_child(option, self._config_option_unit).get_attribute('value') == unit]

        if not matching_options:
            return False

        return matching_options[0]

    def delete_option(self, unit):
        option = self.config_option(unit)

        assert option, f'Cannot delete option "{unit}", could not find matching option'

        delete_button = self._find_child(option, self._delete_config_option_button)
        delete_button.click()

