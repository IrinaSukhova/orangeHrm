# Test case 10 - verify folders creation functionality
#  Open the application
#  Login
#  Click on Reports and Analytics
#  Click on New Folder
#  Fill in the folder name
#  Click Save
#  Verify that New Folder appeared in the list of folders

import time

from helpers.utils import Utils

random_name = Utils.generate_random_string(15)


def test_case_10_verify_folders_creation_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Reports and Analytics")
    app.orangeHrm.employeeManagement.wait_for_loading_bar_gone()
    app.orangeHrm.reportAnalytics.click_on_add_folder()
    print(random_name)
    app.orangeHrm.popUp.input_report_name(random_name)
    app.orangeHrm.popUp.click_save_name_folder()
    app.orangeHrm.reportAnalytics.get_list_reports_name()
    app.assert_that(app.orangeHrm.reportAnalytics.get_list_reports_name()).contains(random_name)
