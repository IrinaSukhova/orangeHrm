# Test Case 1: Verify Attendance Sheets Display
# Description: Verify that the Attendance Sheets are displayed correctly.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Attendance Sheets section
# 4. Verify that the Attendance Sheets table is displayed with correct columns
# Expected Result: The Attendance Sheets table is displayed with columns for Employee Id, Employee Name, Supervisor(s), Regular Time, Extra Time, and Total Leave.

from helpers.csv_helper import CSVHelper
from helpers.utils import Utils

expected_list_of_header = ['Employee Id', 'Employee Name', 'Supervisor(s)', 'Regular Time', 'Extra Time', 'Total Leave Time', 'Total Time', 'Status']

def test_case_1_final_project_verify_attendance_sheets_display(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
    app.orangeHrm.attendance.scroll_to_table_headers()
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
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
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
# 4. Enter an Employee Name in the Employee Name field
# 5. Verify that the table updates to reflect the entered Employee Name
# Expected Result: The Attendance Sheets table updates to show records matching the entered Employee Name.

def test_case_3_final_project_filter_attendance_sheets_by_employee_name(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.enter_employee_name("Adella Lopez")
    app.orangeHrm.attendance.wait_page_load()
    app.assert_that(app.orangeHrm.attendance.table.get_column_data('employee_name')).contains_only("Adella Lopez")



# Test Case 4: Export Attendance Sheets to CSV
# Description: Verify that the Attendance Sheets can be exported to CSV.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Click on the CSV button
# 5.  Verify that a CSV file is generated and downloaded containing the Attendance Sheets data
# Expected Result: A CSV file is generated and downloaded containing the Attendance Sheets data.

def test_case_4_final_project_export_attendance_sheets_to_CSV(app):
    Utils.clear_download_directory()
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
    app.orangeHrm.attendance.export_to_csv()
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("employee_id"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 0, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("employee_name"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 1, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("supervisor"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 2, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("regular_time"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 3, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("extra_time"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 4, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("total_leave_time"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 5, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("total_time"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 6, True)))
    app.assert_that(sorted(app.orangeHrm.attendance.table.get_column_data("status"))).is_equal_to(sorted(CSVHelper.get_column_values('Attendance+Sheets', 7, True)))




# Test Case 5: Filter Attendance Sheets by Supervisor Name
# Description: Verify that the Attendance Sheets can be filtered by Supervisor Name.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Enter a Supervisor Name in the Supervisor Name field
# 5.  Verify that the table updates to reflect the entered Supervisor Name
# Expected Result: The Attendance Sheets table updates to show records matching the entered Supervisor Name.
def test_case_5_final_project_filter_attendance_sheets_by_supervisor_name(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.enter_supervisor_name("Eric Harris")
    app.orangeHrm.attendance.table_is_present()
    app.assert_that(app.orangeHrm.attendance.table.get_column_data("supervisor")).contains("Eric Harris")


# Test Case 6: Filter Attendance Sheets by Job Title
# Description: Verify that the Attendance Sheets can be filtered by Job Title.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Enter a Job Title in the Job Title field
# 5.  Verify that the table updates to reflect the entered Job Title
# Expected Result: The Attendance Sheets table updates to show records matching the entered Job Title.
def test_case_6_final_project_filter_attendance_sheets_by_job_title(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.set_job_title("Art Director")
    app.orangeHrm.attendance.wait_page_load()
    app.assert_that(app.orangeHrm.attendance.table.get_column_data("employee_name")).contains("Ralph Edwards")




# Test Case 7: Verify Data Format Selection
# Description: Verify that the Data Format selection works correctly.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Select a different Data Format from the dropdown
# 5.  Verify that the data is displayed in the selected format
# Expected Result: The Attendance Sheets table updates to display data in the selected format.
def test_case_7_final_project_verify_data_format_selection(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
    a = (app.orangeHrm.attendance.table.get_column_data('regular_time'))
    app.orangeHrm.attendance.set_data_format("HH.HH (8.25)")
    app.orangeHrm.attendance.wait_page_load()
    b = (app.orangeHrm.attendance.table.get_column_data('regular_time'))
    app.assert_that(a).is_not_equal_to(b)


# Test Case 8: Verify Include Filter Functionality
# Description: Verify that the Include filter works correctly.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Select a different option from the Include dropdown (e.g., Current Employees, Past Employees)
# 5.  Verify that the table updates to reflect the selected inclusion criteria
# Expected Result: The Attendance Sheets table updates to show records based on the selected inclusion criteria.
def test_case_8_final_project_Verify_include_filter_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
    app.orangeHrm.attendance.set_include("Current Employees Only")
    app.orangeHrm.attendance.wait_page_load()
    a = (app.orangeHrm.attendance.table.get_column_data('employee_name'))
    app.orangeHrm.attendance.set_include("Current and Past Employees")
    app.orangeHrm.attendance.wait_page_load()
    b = (app.orangeHrm.attendance.table.get_column_data('employee_name'))
    app.assert_that(a).is_equal_to(b)

# Test Case 9: Display Leave Types Checkbox Functionality
# Description: Verify the functionality of the Display Leave Types checkbox.
# Test Steps:
# 1.  Open the application
# 2.  Login
# 3.  Go to Attendance Sheets section
# 4.  Check the Display Leave Types checkbox
# 5.  Verify that the leave types are displayed in the Attendance Sheets table
# 6.  Uncheck the Display Leave Types checkbox
# 7.  Verify that the leave types are hidden in the Attendance Sheets table
# Expected Result: The Attendance Sheets table updates to show/hide leave types based on the checkbox state.
def test_case_9_final_project_Display_leave_types_checkbox_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Attendance")
    app.orangeHrm.attendance.wait_page_load()
    app.orangeHrm.attendance.table_is_present()
    app.orangeHrm.attendance.scroll_to_table_headers()
    a = sorted(app.orangeHrm.attendance.get_list_of_headers())
    app.orangeHrm.attendance.click_checkbox()
    app.orangeHrm.attendance.wait_page_load()
    b = sorted(app.orangeHrm.attendance.get_list_of_headers())
    app.assert_that(a).is_not_equal_to(b)
