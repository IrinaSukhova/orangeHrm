import os.path

from helpers.utils import Utils

random_first_name = Utils.generate_random_string(length=5)
random_last_name = Utils.generate_random_string(length=5)
random_email = Utils.generate_random_email(length=5)


def test_case_12_lesson_28(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitment.wait_for_page_loaded()
    app.orangeHrm.recruitment.click_add_candidate_button()
    app.orangeHrm.popUp.recruitment_add_candidate.set_first_name(random_first_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_last_name(random_last_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_email(random_email)
    #app.orangeHrm.popUp.recruitment_add_candidate.upload_resume('C:/Users/isukhova/PycharmProjects/orangeHrm/files/test_upload.txt')
    resume_path = os.path.join(Utils.get_project_root(), "files", "test_upload.txt") # Adjust the file name as needed
    app.orangeHrm.popUp.recruitment_add_candidate.upload_resume(resume_path)
    app.orangeHrm.popUp.recruitment_add_candidate.click_save()
    app.orangeHrm.recruitment.wait_for_page_loaded()
    #app.assert_that(app.orangeHrm.recruitment.get_action_message()).is_equal_to("Successfully Saved")
    first_and_last_names = app.orangeHrm.recruitment.table[0]['name'].split(' ')
    first_name = first_and_last_names[0]
    last_name = first_and_last_names[1]
    app.assert_that(first_name).is_equal_to(random_first_name)
    app.assert_that(last_name).is_equal_to(random_last_name)


