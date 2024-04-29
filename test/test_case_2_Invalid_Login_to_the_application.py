
def test_case_1_login_to_the_application(app):
    app.orangeHrm.open_application_and_login()
    app.assert_that(app.orangeHrm.get_username_error()).is_equal_to('Username cannot be empty')
    app.assert_that(app.orangeHrm.get_password_error()).is_equal_to('Password cannot be empty')