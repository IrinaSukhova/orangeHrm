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

random_name = Utils.generate_random_string()


def test_case_10_verify_folders_creation_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Reports and Analytics")
    app.orangeHrm.reportAnalytics.wait_for_page_loading()
    app.orangeHrm.reportAnalytics.click_on_add_folder()
    app.orangeHrm.reportAnalytics.input_report_name(random_name)
    app.orangeHrm.reportAnalytics.click_save_name_folder()
    app.orangeHrm.reportAnalytics.wait_for_page_loading()
    app.assert_that(app.orangeHrm.reportAnalytics.get_list_reports_name()).contains(random_name)
    app.orangeHrm.reportAnalytics.find_and_click_delete_button_for_folder(random_name)
    app.orangeHrm.reportAnalytics.confirm_folder_deleting()
    app.assert_that(app.orangeHrm.reportAnalytics.get_manipulation_meassage_text()).is_equal_to("Successfully Deleted")
    app.assert_that(app.orangeHrm.reportAnalytics.get_list_reports_name()).does_not_contain(random_name)