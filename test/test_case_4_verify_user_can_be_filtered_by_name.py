# Test Case 4: Verify that a user can be filtered by username
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of an existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display only the user(s) matching the entered username.

import pytest

@pytest.mark.group1
def test_case_4_verify_user_can_be_filtered_by_name(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_user_name_filter('Admin')
    app.orangeHrm.popUp.click_on_search()
    app.assert_that(app.orangeHrm.hrAdministration.get_list_of_user_names()).is_equal_to(['Admin'])