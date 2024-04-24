# Test Case 7: Verify Employee Name Autocomplete Suggestion
# Test Name: Test_Employee_Name_Autocomplete
# Purpose: To verify that the autocomplete suggests names based on the entered value in the 'Employee Name' field.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Start typing a known employee name in the 'Employee Name' field.
# Expected Result:
# As the user types, an autocomplete dropdown should appear with employee name suggestions.

# -----------------------------------------------------------------------------------

# Test Case 7_1: Verify No Results Found Error Message
# Test Name: Test_Employee_Name_No_Results
# Purpose: To verify that an appropriate error message is shown when no employee names match the entered value.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Enter a non-existing employee name in the 'Employee Name' field.
# Expected Result:
# A message indicating 'no results found' should appear if no employee names match the entered value.

# -----------------------------------------------------------------------------------

# Test Case 7_2: Verify Dropdown Default Values
# Test Name: Test_Dropdown_Default_Values
# Purpose: To verify that the dropdowns in the 'Filter Users' pop-up are set to their default values upon opening.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Get default values from all drop-downs (you should create a separate method for each drop-down)
# 6. Assert values from all drop-downs in test (you should assert values separately for each drop-down) using assert_that(['a','b']).is_equal_to(['a','b'])
# Expected Result:
# All dropdowns in the 'Filter Users' pop-up should display their default values.

# -----------------------------------------------------------------------------------

# Test Case 7_3: Verify Reset Button Functionality
# Test Name: Test_Reset_Button
# Purpose: To verify that the 'Reset' button clears all input fields and selections and closes the 'Filter Users' pop-up.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Reset' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Reset' button and upon reopening, all input fields and dropdowns should be reset to their default selections.

# -----------------------------------------------------------------------------------

# Test Case 7_4: Verify Cancel Button Functionality
# Test Name: Test_Cancel_Button
# Purpose: To verify that the 'Cancel' button closes the 'Filter Users' pop-up without clearing selected values.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Cancel' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Cancel' button and upon reopening, the previously selected values should be retained.

def test_case_7_Verify_Employee_Name_Autocomplete_Suggestion(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_employee_name('Odis')
    app.assert_that(app.orangeHrm.popUp.get_autocomplete_names()).contains('Odis Adalwin', 'Kgosi Modise')

def test_case_7_1_Verify_No_Results_Found_Error_Message(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_employee_name('Murat')
    app.assert_that(app.orangeHrm.popUp.get_no_results_message()).is_equal_to('No results found')

def test_case_7_2_Verify_Dropdown_Default_Values(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_dropdown_values()).is_equal_to(['All','Default ESS'])
    app.assert_that(app.orangeHrm.popUp.get_admin_role_dropdown_values()).is_equal_to(['All', 'Global Admin', 'Leave Admin', 'Regional HR Admin', 'Report Admin'])
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_dropdown_values()).is_equal_to(['All', 'Default Supervisor'])
    app.assert_that(app.orangeHrm.popUp.get_status_dropdown_values()).is_equal_to(['All', 'Enabled', 'Disabled'])
    app.assert_that(app.orangeHrm.popUp.get_location_dropdown_values()).is_equal_to(['-- Select --', 'All', 'Australia', 'Australia office', 'Canada', 'Canadian Development Center', 'France', 'France Office', 'Germany', 'German Office', 'India', 'India Office', 'Jamaica', 'Jamaica training center', 'Mexico', 'Mexico Office', 'Philippines', 'Philippine call center', 'Singapore', 'Singapore Regional HQ', 'South Africa', 'South Africa Satellite Office', 'United Kingdom', 'UK Office', 'United States', 'US Office'])

def test_case_7_3_Verify_Reset_Button_Functionality(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    # app.orangeHrm.popUp.set_hr_administration_drop_downs(ess_role="Default ESS", user_name="Admin")
    app.orangeHrm.popUp.set_username("Admin")
    app.orangeHrm.popUp.set_employee_name("wer")
    app.orangeHrm.popUp.set_ess_role_input_dropdown("Default ESS")
    app.orangeHrm.popUp.set_admin_role_input_dropdown("Leave Admin")
    app.orangeHrm.popUp.set_supervisor_role_dropdown("Default Supervisor")
    app.orangeHrm.popUp.set_status_input_dropdown("Disabled")
    app.orangeHrm.popUp.set_location_input_dropdown("Australia")
    app.orangeHrm.popUp.click_on_filter_reset_button()
    app.orangeHrm.popUp.wait_filter_pop_up_stop_displayed()
    app.orangeHrm.hrAdministration.click_on_filter()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_selected_dropdown_value()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_admin_role_selected_dropdown_value()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_selected_dropdown_value()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_status_selected_dropdown_value()).is_empty()
    app.assert_that(app.orangeHrm.popUp.get_location_selected_dropdown_value()).is_equal_to("All")

def test_case_7_4_Verify_Cancel_Button_Functionality(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.click_on_filter_reset_button()
    app.orangeHrm.popUp.wait_filter_pop_up_stop_displayed()
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_username("Admin")
    app.orangeHrm.popUp.set_employee_name("wer")
    app.orangeHrm.popUp.set_ess_role_input_dropdown("Default ESS")
    app.orangeHrm.popUp.set_admin_role_input_dropdown("Leave Admin")
    app.orangeHrm.popUp.set_supervisor_role_dropdown("Default Supervisor")
    app.orangeHrm.popUp.set_status_input_dropdown("Disabled")
    app.orangeHrm.popUp.set_location_input_dropdown("Australia")
    app.orangeHrm.popUp.click_on_filter_cancel_button()
    app.orangeHrm.popUp.wait_filter_pop_up_stop_displayed()
    app.orangeHrm.hrAdministration.click_on_filter()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_selected_dropdown_value()).is_equal_to("Default ESS")
    app.assert_that(app.orangeHrm.popUp.get_admin_role_selected_dropdown_value()).is_equal_to("Leave Admin")
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_selected_dropdown_value()).is_equal_to("Default Supervisor")
    app.assert_that(app.orangeHrm.popUp.get_status_selected_dropdown_value()).is_equal_to("Disabled")
    app.assert_that(app.orangeHrm.popUp.get_location_selected_dropdown_value()).contains("Australia office")