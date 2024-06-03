# Test Case 1: Verify Attendance Sheets Display
# Description: Verify that the Attendance Sheets are displayed correctly.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Attendance Sheets section
# 4. Verify that the Attendance Sheets table is displayed with correct columns
# Expected Result: The Attendance Sheets table is displayed with columns for Employee Id, Employee Name, Supervisor(s), Regular Time, Extra Time, and Total Leave.
from helpers.utils import Utils

expected_list_of_header = ['Employee Id', 'Employee Name', 'Supervisor(s)', 'Regular Time', 'Extra Time', 'Total Leave Time', 'Total Time', 'Status']

def test_case_1_final_project_verify_attendance_sheets_display(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_present()
    app.assert_that(app.orangeHrm.attendance.get_list_of_headers()).is_equal_to(expected_list_of_header)



# Test Case 2: Filter Attendance Sheets by Pay Period
# Description: Verify that the Attendance Sheets can be filtered by Pay Period.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Attendance Sheets section
# 4. Select a different Pay Period from the dropdown
# 5. Verify that the table updates to reflect the selected Pay Period
# Expected Result: The Attendance Sheets table updates to show records for the selected Pay Period.

def test_case_2_final_project_filter_attendance_sheets_by_pay_period(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_present()
    a = app.orangeHrm.attendance.table.get_column_data('employee_id')
    app.orangeHrm.attendance.new_pay_period('2023-05-28 - 2023-06-03')
    b = app.orangeHrm.attendance.table.get_column_data('employee_id')
    app.assert_that(sorted(a)).is_not_equal_to(sorted(b))


# Test Case 3: Filter Attendance Sheets by Employee Name
# Description: Verify that the Attendance Sheets can be filtered by Employee Name.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Attendance Sheets section
# 4. TODO - Enter an Employee Name in the Employee Name field
# 5. TODO - Verify that the table updates to reflect the entered Employee Name
# Expected Result: The Attendance Sheets table updates to show records matching the entered Employee Name.


def test_case_3_final_project_filter_attendance_sheets_by_employee_name(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_present()
    app.orangeHrm.attendance.enter_employee_name("Adella Lopez")
    app.orangeHrm.attendance.wait_page_present()
    app.assert_that(app.orangeHrm.attendance.table.get_column_data('employee_name')).contains_only("Adella Lopez")






# Test Case 4: Export Attendance Sheets to CSV
# Description: Verify that the Attendance Sheets can be exported to CSV.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Click on the CSV button
# 5. TODO - Verify that a CSV file is generated and downloaded containing the Attendance Sheets data
# Expected Result: A CSV file is generated and downloaded containing the Attendance Sheets data.

# Test Case 5: Filter Attendance Sheets by Supervisor Name
# Description: Verify that the Attendance Sheets can be filtered by Supervisor Name.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Enter a Supervisor Name in the Supervisor Name field
# 5. TODO - Verify that the table updates to reflect the entered Supervisor Name
# Expected Result: The Attendance Sheets table updates to show records matching the entered Supervisor Name.

# Test Case 6: Filter Attendance Sheets by Job Title
# Description: Verify that the Attendance Sheets can be filtered by Job Title.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Enter a Job Title in the Job Title field
# 5. TODO - Verify that the table updates to reflect the entered Job Title
# Expected Result: The Attendance Sheets table updates to show records matching the entered Job Title.

# Test Case 7: Verify Data Format Selection
# Description: Verify that the Data Format selection works correctly.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Select a different Data Format from the dropdown
# 5. TODO - Verify that the data is displayed in the selected format
# Expected Result: The Attendance Sheets table updates to display data in the selected format.

# Test Case 8: Verify Include Filter Functionality
# Description: Verify that the Include filter works correctly.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Select a different option from the Include dropdown (e.g., Current Employees, Past Employees)
# 5. TODO - Verify that the table updates to reflect the selected inclusion criteria
# Expected Result: The Attendance Sheets table updates to show records based on the selected inclusion criteria.

# Test Case 9: Display Leave Types Checkbox Functionality
# Description: Verify the functionality of the Display Leave Types checkbox.
# Test Steps:
# 1. TODO - Open the application
# 2. TODO - Login
# 3. TODO - Go to Attendance Sheets section
# 4. TODO - Check the Display Leave Types checkbox
# 5. TODO - Verify that the leave types are displayed in the Attendance Sheets table
# 6. TODO - Uncheck the Display Leave Types checkbox
# 7. TODO - Verify that the leave types are hidden in the Attendance Sheets table
# Expected Result: The Attendance Sheets table updates to show/hide leave types based on the checkbox state.
