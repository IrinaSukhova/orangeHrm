# Test Case: Add Course and Verify the Coordinator

# Step 1: Open the application
# Step 2: Login
# Step 3: Go to Training section from the side menu
# Step 4: Filter coordinator by name 'Aaron Hamilton'
# Step 5: Click on 'Filter by' button
# Step 6: Set the coordinator by name Aaron Hamilton
# Step 7: Click on 'Search'
# Step 8: Get the list of titles assigned to selected coordinator
# Step 9: Click on 'Add Course' button
# Step 10: Fill in all required fields, including setting coordinator 'Aaron Hamilton'
# Step 11: Click on 'Save' button
# Step 12: Go back to training table and filter by coordinator again
# Step 13: Verify that list of trainings increased with the new value that has been added in previous steps

from helpers.utils import Utils

title_random = Utils.generate_random_string(10)

def test_case_13_lesson_31_Add_Course_and_Verify_the_Coordinator(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Training")
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.step.switch_to_iframe(app.orangeHrm.training.iframe)
    app.orangeHrm.training.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.training_filter.get_filter_courses_header_text()).is_equal_to("Filter Courses")
    app.orangeHrm.popUp.training_filter.set_coordinator("Brody Alan")
    app.orangeHrm.popUp.training_filter.click_on_search()
    app.orangeHrm.training.wait_filtered_table()
    list_before_add_course = app.orangeHrm.training.table.get_column_data('title')
    app.orangeHrm.training.click_on_add_course_button()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.popUp.training_add_course.set_title(title_random)
    app.orangeHrm.popUp.training_add_course.set_coordinator("Brody Alan")
    app.orangeHrm.popUp.training_add_course.click_save()
    app.orangeHrm.training.click_on_go_to_courses_button()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_filter_button()
    app.orangeHrm.popUp.training_filter.set_coordinator("Brody Alan")
    app.orangeHrm.popUp.training_filter.click_on_search()
    app.orangeHrm.training.wait_filtered_table()
    list_containing_new_course = list_before_add_course + [title_random]
    app.assert_that(sorted(app.orangeHrm.training.table.get_column_data('title'))).is_equal_to(sorted(list_containing_new_course))

