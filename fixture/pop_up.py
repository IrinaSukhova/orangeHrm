from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#systemuser_uname_filter'
    employee_name_field = '#selectedEmployee_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = '//input[@id="systemuser_uname_filter"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    filter_search_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Search"]'
    pass_required_message = '//input[@id="password"]/following::span[text()="Required"]'
    confirm_pass_required_message = '//input[@id="confirmpassword"]/following::span[text()="Required"]'
    pass_length_message = '//input[@id="password"]/following::span[text()="Your password should have at least 8 characters."]'
    pass_strength_message = '.password-strength-check'
    empty_space = '.password-help-text-container small'
    password_error_massage = '//input[@id="password"]/following-sibling::span'
    confirm_password_error_massage = '//input[@id="confirmpassword"]/following-sibling::span'
    strength_indicator = '.password-strength-check'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search_button)

    def get_strength_indicator_text(self):
        self.step.specified_element_is_present(self.strength_indicator, 5)
        return self.step.get_element_text(self.strength_indicator)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_massage)

    def get_confirm_password_error(self):
        return self.step.get_element_text(self.confirm_password_error_massage)