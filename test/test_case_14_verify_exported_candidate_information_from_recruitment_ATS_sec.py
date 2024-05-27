# Test Case: Verify Exported Candidate Information from Recruitment ATS Section
# Step 1:  Open the application
# Step 2:  Login
# Step 3:  Go to Recruitment ATS section
# Step 4:  Filter candidates
# Step 5:  Open the filter and fill in the job title "Customer Support Specalist"
# Step 6:  Click on 'Search' button
# Step 7:  Click on 'Export to CSV' button
# Step 8:  Once CSV is exported, open it
# Step 9:  Verify that information from the table in the application corresponds to information in the exported CSV file

from helpers.csv_helper import CSVHelper
from helpers.utils import Utils


def test_case_14_lesson32_verify_exported_candidate_information_from_recruitment_ATS_sec(app):
    Utils.clear_download_directory()
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.click_on_filter_button()
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.set_search('Customer Support Specalist')
    app.orangeHrm.recruitmentAts.click_search_button()
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.export_to_csv()
    vacancy_name = CSVHelper.get_column_values('RecruitmentReport', 0, partial_name=True)
    candidate_name = CSVHelper.get_column_values('RecruitmentReport', 1, partial_name=True)
    date_of_application = CSVHelper.get_column_values('RecruitmentReport', 2, partial_name=True)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('vacancy')).is_equal_to(vacancy_name)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('name')).is_equal_to(candidate_name)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('date_applied')).is_equal_to(date_of_application)