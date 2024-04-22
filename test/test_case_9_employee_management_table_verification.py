#import time

list_of_expected_employee_id = ['1061']
list_of_expected_employee_name = ['Mazie Abraham']
list_of_employment_status = ['Full-Time Permanent']


def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    #app.orangeHrm.employeeManagement.wait_for_table1()
    a = app.orangeHrm.employeeManagement.table.get_column_data('employee_id')
    b = app.orangeHrm.employeeManagement.table.get_column_data('employee_name')
    c = app.orangeHrm.employeeManagement.table.get_column_data('job_title')
    d = app.orangeHrm.employeeManagement.table.get_column_data('employment_status')
    e = app.orangeHrm.employeeManagement.table[1]['employee_id']
    f = app.orangeHrm.employeeManagement.table[0]['employee_name']
    g = app.orangeHrm.employeeManagement.table[4]['employment_status']
    app.assert_that(e).is_equal_to('1061')
    app.assert_that(f).is_equal_to('Mazie Abraham')
    app.assert_that(g).is_equal_to('Full-Time Permanent')


    # 1 Create a new object of the table class inside the employee management component (based on the example from hr_administration).
    # 2 Find selectors: For list of rows and list of column elements (Employee Id, Name, Job Title, Employment Status).
    # 3 Get list of elements from each defined column and assert them with the expected one.
    # 4 Get second element from the 'Employee Id' column and assert it with the expected one.
    # 5 Get first element from the 'Name' column and assert it with the expected one.
    # 6 Get fifth element from the 'Employment Status' column and assert it with the expected one.

def test_case_9_1_employee_management_table_filtering(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.click_on_filter_button()



    # TODO: Click on the filter button in the Employee Management section
    # TODO: In the filter pop-up, set 'Employment Status' to 'Full-Time Contract'
    # TODO: Set 'Location' to 'Canada'
    # TODO: Click the search button
    # TODO: Wait for the table to load (ensure the table is refreshed with the filter applied)
    # TODO: Using the previously created table component, get list of users Names and Assert the list of users with the expected ones
    # TODO: Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    # TODO: Get list of 'Locations' for each listed user and assert it with the expected 'Canada'

def test_case_9_2_employee_management_table_location_change(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")

    # TODO: Click on the filter button in the Employee Management section
    # TODO: In the filter pop-up, set 'Employment Status' to 'Full-Time Contract'
    # TODO: Set 'Location' to 'Canada'
    # TODO: Click the search button
    # TODO: Wait for the table to load (ensure the table is refreshed with the filter applied)
    # TODO: Using the previously created table component, get list of users and Assert the list of users with the expected ones
    # TODO: Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    # TODO: Get list of 'Locations' for each listed user and assert it with the expected 'Canada'

    # TODO: Click on the filter button again in the Employee Management section
    # TODO: Change 'Location' to 'Australia'
    # TODO: Click the search button
    # TODO: Wait for the table to load (ensure the table is refreshed with the new location)
    # TODO: Using the previously created table component, get list of users and Assert the list of users with the expected ones
    # TODO: Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    # TODO: Get list of 'Locations' for each listed user and assert it with the expected 'Australia'