# Test Case 8: Verify Retrieval of Widget Names in Employee Management Component
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
# 8. Verify that the list of retrieved widget names matches the expected list.
# Expected Result:
# The 'get_widget_names' method should return an accurate list of widget names from the side menu. Then assert it with the expected one.

list_of_expected_widgets = ['Quick Access', 'Time At Work', 'Employees on Leave Today', 'Latest News', 'Latest Documents', 'Performance Quick Feedback', "Current Year's Leave Taken by Department", 'Buzz Latest Posts', 'Leave Taken on Each Day of the Week Over Time', 'Leave Scheduled in Each Month', 'Leave Taken on Each Calendar Month Over the Years', 'Headcount by Location', 'Annual Basic Payment by Location', 'My Actions']

def test_case_8_verify_retrieval_of_widget_names_in_employee_management_component(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.click_home()
    app.assert_that(app.orangeHrm.employeeManagement.get_widgets_headers().sort()).is_equal_to(list_of_expected_widgets.sort())