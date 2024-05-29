# Test Case: Verify Error Message in Leave Section with Future Dates
# Step 1:  Open the application
# Step 2:  Login
# Step 3:  Go to Leave section
# Step 4:  Select some date far, far away in the future from the calendar for the 'From' field
# Step 5:  Select some day in the future, in the far, far away future for the 'To' field from the calendar
# Step 6:  Click on 'Search' button
# Step 7:  Verify that message 'No records found' is displayed
import time

def test_case_15_lesson33_verify_error_message_in_leave_section(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Leave")
    app.orangeHrm.leave.wait_calendar_displayed()
    app.orangeHrm.leave.open_calendar_from()
    app.orangeHrm.leave.calendar.set_date('11-15-2025')
    app.orangeHrm.leave.open_calendar_to()
    app.orangeHrm.leave.calendar.set_date('01-13-2028')
    app.orangeHrm.leave.click_search_button()
    app.assert_that(app.orangeHrm.leave.get_search_message()).is_equal_to("No Records Found")



# Test Case: Verify Recruitment ATS Table Based on Selected Date
# Step 1:  Open the application
# Step 2:  Login
# Step 3:  Go to Recruitment ATS section
# Step 4:  Click on 'Filter Candidates' button
# Step 5:  Set the 'Date Applied From' field using the calendar with a valid date where records exist
# Step 6:  Click on 'Search' button
# Step 7:  Verify that table results correspond to that date

def test_case_15_2_lesson33_verify_recruitmentATS_table_based_on_selected_date(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.click_on_filter_button()
    app.orangeHrm.popUp.recruitmentAts_filter.wait_for_displayed()
    app.orangeHrm.popUp.recruitmentAts_filter.click_date_applied_from()
    app.orangeHrm.popUp.recruitmentAts_filter.calendar.set_date('09-27-2023')
    app.orangeHrm.recruitmentAts.click_search_button()


