import time
import pytest

list_of_expected_widgets = ['Quick Access', 'Time At Work', 'Employees on Leave Today', 'Latest News', 'Latest Documents', 'Performance Quick Feedback', "Current Year's Leave Taken by Department", 'Buzz Latest Posts', 'Leave Taken on Each Day of the Week Over Time', 'Leave Scheduled in Each Month', 'Leave Taken on Each Calendar Month Over the Years', 'Headcount by Location', 'Annual Basic Payment by Location', 'My Actions']
list_of_expected_configurations = ['Annual Basic Payment by Location', 'Buzz Latest Posts', "Current Year's Leave Taken by Department", 'Employees on Leave Today', 'Headcount by Location', 'Latest Documents', 'Latest News', 'Leave Scheduled in Each Month', 'Leave Taken on Each Calendar Month Over the Years', 'Leave Taken on Each Day of the Week Over Time', 'My Actions', 'Performance Quick Feedback', 'Quick Access', 'Time At Work']  # Test Case 8: Verify Retrieval of Widget Names in Employee Management Component
# Test Name: Test_Get_Widget_Names_Employee Management
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Log in to the application with valid credentials.
# 3. Navigate to the 'Employee Management' component from the main menu.
# 4. Click on the 'Home' button
# 5. Execute the 'get_widget_names' method to retrieve the list of widget names.
# 6. Verify that the list of retrieved widget names matches the expected list.
# Expected Result:
# The 'get_widget_names' method should return an accurate list of widget names that are present within the Employee Management component.
@pytest.mark.group3
def test_case_8_verify_retrieval_of_widget_names_in_employee_management_component(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.click_home()
    app.assert_that(app.orangeHrm.employeeManagement.get_widgets_headers().sort()).is_equal_to(list_of_expected_widgets.sort())



# Test Case 8_1: Verify Retrieval of Widget Names in Employee Management Component inside the Configuration
# Test Name: Test_Get_Widget_Names_Employee_Management Configuration section
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Log in to the application with valid credentials.
# 3. Navigate to the 'Employee Management' component from the main menu.
# 4. Click on the 'Home' button.
# 5. Click on gear button.
# 6. In side menu click on "My Widgets".
# 7. Get list of widgets names.
# 8. Verify that the list of retrieved widget names matches the expected list.tq
# Expected Result:
# The 'get_widget_names' method should return an accurate list of widget names from the side menu. Then assert it with the expected one.
@pytest.mark.group3
def test_case_8_1_verify_retrieval_of_widget_names_in_employee_management_component_inside_the_configuration(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.orangeHrm.employeeManagement.click_home()
    app.orangeHrm.employeeManagement.wait_for_loading_bar_gone()
    app.orangeHrm.employeeManagement.click_gear_button()
    app.orangeHrm.employeeManagement.click_my_widgets_tab()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.get_widgets_names())).is_equal_to(sorted(list_of_expected_configurations))
