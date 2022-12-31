import pytest
from pages import edit_exercise_page, browse_exercise_page
from .testing_utilities.mock_data_generation import random_string

import time


@pytest.mark.exercise
class TestCreateExercise:
    @pytest.fixture
    def page(self, driver):
        return edit_exercise_page.EditExercisePage(driver, 'create')

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_add_config_option(self, page):
        page.fill_form('title', 'description', [("weight", "lbs")])
        assert page.config_option('lbs'), "Could not add config option, cannot find matching config option unit"

    @pytest.mark.midweight
    @pytest.mark.dependency(depends=['test_add_config_option'])
    def test_delete_config_option(self, page):
        page.fill_form('title', 'description', [('weight', 'lbs'), ('distance', 'meters')])
        page.delete_option('lbs')

        assert not page.config_option('lbs'), "Failed to delete config option - it is still present"

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_create_exercise(self, page):
        ex_title = random_string(10)
        ex_description = random_string(20)
        page.create_exercise(ex_title, ex_description, [("weight","lbs"),("duration","seconds")])
        assert page.success_message_present(), "Failed to create exercise, could not find success message"

        browse_page = browse_exercise_page.BrowseExercisePage(page.driver)
        exercise = browse_page.get_exercise(ex_title)

        assert exercise, f"Failed to create exercise {ex_title}, Could not find matching card on browse page"
        assert exercise['description'] == ex_description, "Failed to create exercise, " \
                                                          "browse card's description does not match"

    @pytest.mark.midweight
    @pytest.mark.dependency(depends=['test_create_exercise'])
    def test_delete_exercise(self, page):
        ex_title = random_string(10)
        ex_description = random_string(20)
        page.create_exercise(ex_title, ex_description, [("weight","lbs"),("duration","seconds")])
        assert page.success_message_present(), "Failed to create exercise, could not find success message"

        browse_page = browse_exercise_page.BrowseExercisePage(page.driver)
        exercise = browse_page.get_exercise(ex_title)
        assert exercise, f"Failed to create exercise {ex_title}, so deleting it is impossible"

        browse_page.delete_exercise(ex_title)
        assert not browse_page.get_exercise(ex_title), f"Failed to delete exercise {ex_title}, " \
                                                       f"it's still present on the browse page"
