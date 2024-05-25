# Test Case: Verification of Added Course
# Step 1:  Open the application
# Step 2: Click on 'Training' from the side menu
# Step 3: Click on 'Add Course' button
# Step 4: Add title to the course
# Step 5: Add coordinator
# Step 6: Click on 'Save' button
# Step 7: Go to 'Courses'
# Step 8: Click on 'Filter' button
# Step 9: Add the title of the created course in the filter
# Step 10:Click 'Search'
# Step 11:Verify that the created course is displayed in the table

from helpers.utils import Utils

title_random = Utils.generate_random_string()

def test_case_11_lesson27_veriffication_of_added_course(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Training")
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.step.switch_to_iframe(app.orangeHrm.training.iframe)
    app.orangeHrm.training.click_on_add_course_button()
    app.orangeHrm.popUp.training_add_course.set_title(title_random)
    app.orangeHrm.popUp.training_add_course.set_coordinator("Odis Adalwin")
    app.orangeHrm.popUp.training_add_course.click_save()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_go_to_courses_button()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_filter_button()
    app.orangeHrm.popUp.training_filter.search_training(title_random)
    app.orangeHrm.popUp.training_filter.click_on_search()
    app.orangeHrm.training.wait_filtered_table()
    app.assert_that(app.orangeHrm.training.table.get_column_data('title')).contains(title_random)
