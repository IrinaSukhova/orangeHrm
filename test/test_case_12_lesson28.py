from helpers.utils import Utils

random_first_name = Utils.generate_random_string()
random_last_name = Utils.generate_random_string()
random_email = Utils.generate_random_email()


def test_case_12_lesson_28(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitment.click_add_candidate_button()
    app.orangeHrm.popUp.recruitment_add_candidate.set_first_name(random_first_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_last_name(random_last_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_email(random_email)
    app.orangeHrm.popUp.recruitment_add_candidate.upload_resume('C:/Users/isukhova/PycharmProjects/orangeHrm/files/test_upload.txt')
    app.orangeHrm.popUp.recruitment_add_candidate.click_save()
    app.orangeHrm.recruitment.wait_for_page_loaded()
    first_and_last_names = app.orangeHrm.recruitment.table[0]['name'].split(' ')
    first_name = first_and_last_names[0]
    last_name = first_and_last_names[1]
    app.assert_that(first_name).is_equal_to(random_first_name)
    app.assert_that(last_name).is_equal_to(random_last_name)


