# Test Case: Verification of Added Course
# Step 1: TODO - Open the application
# Step 2: TODO - Click on 'Training' from the side menu
# Step 3: TODO - Click on 'Add Course' button
# Step 4: TODO - Add title to the course
# Step 5: TODO - Add coordinator
# Step 6: TODO - Click on 'Save' button
# Step 7: TODO - Go to 'Courses'
# Step 8: TODO - Click on 'Filter' button
# Step 9: TODO - Add the title of the created course in the filter
# Step 10: TODO - Click 'Search'
# Step 11: TODO - Verify that the created course is displayed in the table

import pytest
def test_case_11_veriffication_of_added_course(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Training")
    app.orangeHrm.training.click_on_add_course_button()
    app.orangeHrm.popUp.training_filter.set_title("Test1")
