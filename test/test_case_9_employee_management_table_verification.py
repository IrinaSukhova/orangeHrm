def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")

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