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