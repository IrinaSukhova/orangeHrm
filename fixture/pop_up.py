import email
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper


class PopUp:
    user_name_field = '#user_name'
    employee_name_field = '#selectedEmployee_value'
    employee_name_filter_field = '#employee_name_filter_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = '#systemuser_uname_filter'
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
    autocomplete_dropdown = '#employee_name_filter_dropdown span.angucomplete-title'
    message_no_results = "//div[contains(text(),'No results found')]"
    ess_role_input_field = '#essroles_inputfileddiv input'
    ess_role_dropdown_values = '#essroles_inputfileddiv li'
    supervisor_role_input_field = '#supervisorroles_inputfileddiv input'
    supervisor_role_dropdown_values = '#supervisorroles_inputfileddiv li'
    location_input_field = '#location_inputfileddiv input'
    location_dropdown_values = '#location_inputfileddiv li'
    admin_role_input_field = '#adminroles_inputfileddiv input'
    admin_role_dropdown_values = '#adminroles_inputfileddiv li'
    status_input_field = '#status_inputfileddiv input'
    status_dropdown_values = '#status_inputfileddiv li'
    drop_down_is_expanded = 'input[class="select-dropdown active"]'
    filter_reset_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Reset"]'
    filter_cancel_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Cancel"]'
    searching_text = '//div[@id="employee_name_filter_dropdown"]/div[text()="Searching..."]'
    list_of_found_employee_names = '#employee_name_filter_dropdown div[ng-repeat="result in results"] span[class="angucomplete-title"]'
    employee_name_filter_dropdown_warnings = '//div[@id="employee_name_filter_dropdown" and @class="angucomplete-dropdown"]/div[2]'

    # POpup_employee_filtre
    location_input_field_employee = '//label[text()="Location"]/preceding-sibling::div//input'
    status_input_field_employee = '//label[text()="Employment Status"]/preceding-sibling::div//input[@value="All"]'
    list_of_drop_down_values = 'ul[id^="select-options"][style*="display: block"] li span'
    location_dropdown_employee_values = 'ul[id^="select-options"][style*="display: block"] li'            #'ul[id^="select-options"][style*="display: block"] li span'
    employee_name_filter_dropdown = '.angucomplete-title'

    input_report_name_field = 'input[placeholder="Enter Folder Name"]'
    save_folder_name = 'button[data-test="submitFolderButton"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.training_filter = TrainingFilter(step, wd)
        self.training_add_course = TrainingAddCourse(step, wd)
        self.recruitment_add_candidate = RecruitmentAddCandidate(step, wd)
        self.recruitmentAts_filter = RecruitmentAtsFilter(step, wd)

    def set_username(self, text):
        self.step.click_on_element(self.user_name_field)
        self.step.input_text(self.user_name_field, text)

    def set_user_name_filter(self, text):
        self.step.input_text(self.user_name_filter_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if self.step.specified_element_is_present(self.message_no_results, 3) == False:
            self.step.click_element_containing_text(self.employee_name_filter_dropdown, text)

    def set_employee_name_filter(self, text):
        self.step.input_text(self.employee_name_filter_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if self.step.specified_element_is_present(self.employee_name_filter_dropdown_warnings, 3) == False:
            self.step.click_element_containing_text(self.employee_name_filter_dropdown, text)

    def set_password(self, text):
        self.step.input_text(self.password_field, text)

    def click_on_password_field(self):
        self.step.click_on_element(self.password_field)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def click_on_empty(self):
        self.step.click_on_element(self.empty_space)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search_button)

    def get_strength_indicator_text(self):
        self.step.wait_for_element(self.pass_strength_message, 30)
        time.sleep(0.5)
        return self.step.get_element_text(self.strength_indicator)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_massage)

    def get_confirm_password_error(self):
        return self.step.get_element_text(self.confirm_password_error_massage)

    def get_employee_name_dropdown_text(self):
        self.step.specified_element_is_present(self.employee_name_filter_dropdown, 10)
        return self.step.get_elements_texts(self.employee_name_filter_dropdown)

    def get_no_results_message(self):
        return self.step.get_element_text(self.message_no_results)

    def get_ess_role_dropdown_values(self):
        return self.step.get_elements_texts(self.ess_role_dropdown_values)

    def get_admin_role_dropdown_values(self):
        return self.step.get_elements_texts(self.admin_role_dropdown_values)

    def get_supervisor_role_dropdown_values(self):
        return self.step.get_elements_texts(self.supervisor_role_dropdown_values)

    def get_status_dropdown_values(self):
        return self.step.get_elements_texts(self.status_dropdown_values)

    def get_location_dropdown_values(self):
        return self.step.get_elements_texts(self.location_dropdown_values)

    def get_ess_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.ess_role_input_field, 'value', True)

    def get_admin_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.admin_role_input_field, 'value', True)

    def get_supervisor_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.supervisor_role_input_field, 'value', True)

    def get_status_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.status_input_field, 'value', True)

    def get_location_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.location_input_field, 'value', True)

    def get_filter_table_name(self):
        self.step.wait_for_element(self.filter_popup_table, 20)
        return self.step.get_element_text(self.filter_popup_table)

    def set_ess_role_input_dropdown(self, text):
        self.step.click_on_element(self.ess_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.ess_role_dropdown_values, text)

    def set_admin_role_input_dropdown(self, text):
        self.step.click_on_element(self.admin_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.admin_role_dropdown_values, text)

    def set_supervisor_role_dropdown(self, text):
        self.step.click_on_element(self.supervisor_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.supervisor_role_dropdown_values, text)

    def set_status_input_dropdown(self, text):
        self.step.click_on_element(self.status_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.status_dropdown_values, text)

    def set_location_input_dropdown(self, text):
        self.step.click_on_element(self.location_input_field, True, True)
        time.sleep(0.5)
        self.step.click_element_by_text(self.location_dropdown_employee_values, text)

    def click_on_filter_reset_button(self):
        self.step.click_on_element(self.filter_reset_button)

    def click_on_filter_cancel_button(self):
        self.step.click_on_element(self.filter_cancel_button)

    def wait_filter_pop_up_stop_displayed(self):
        self.step.specified_element_is_not_present(self.filter_popup_table)

    def set_employment_status(self, text):
        self.step.wait_for_element(self.status_input_field_employee, 5)
        self.step.click_on_element(self.status_input_field_employee)
        time.sleep(1)
        self.step.click_element_by_text(self.list_of_drop_down_values, text)

    def set_employee_filter_location(self, text):
        self.step.specified_element_is_present(self.location_input_field_employee, 5)
        self.step.click_on_element(self.location_input_field_employee)
        time.sleep(1)
        self.step.click_element_containing_text(self.location_dropdown_employee_values, text)

    def set_hr_administration_drop_downs(self, user_name=None, employee_name=None, ess_role=None, admin_role=None,
                                         supervisor_role=None, status=None, location=None):
        if user_name is not None:
            self.set_user_name_filter(user_name)
        if employee_name is not None:
            self.set_employee_name_filter(employee_name)
        if ess_role is not None:
            self.set_ess_role_input_dropdown(ess_role)
        if admin_role is not None:
            self.set_admin_role_input_dropdown(admin_role)
        if supervisor_role is not None:
            self.set_supervisor_role_dropdown(supervisor_role)
        if status is not None:
            self.set_status_input_dropdown(status)
        if location is not None:
            self.set_location_input_dropdown(location)


class TrainingFilter:
    title_input_field = '#searchCourse_title'
    iframe = "#noncoreIframe"
    filter_courses_header = '.customized-modal-header h5'
    title_input_field_autocomplete_dropdowns = '.ac_results ul li'
    input_fields_dropdown = '.ac_results ul li'
    filter_search = 'a[id="searchBtn"]'
    coordinator_input_field = 'input[type="text"][name*="coordinator"]'
    coordinator_input_field_dropdown = '.ac_results ul li'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_title(self, title):
        self.step.switch_to_iframe(self.iframe)
        self.step.input_text(self.title_input_field, title)
        self.step.switch_to_default_content()

    def search_training(self,text):
        self.step.input_text(self.title_input_field, text)
        self.step.wait_for_element(self.input_fields_dropdown, 10)
        self.step.click_element_containing_text(self.input_fields_dropdown, text)

    def set_coordinator(self, text):
        self.step.input_text(self.coordinator_input_field, text)
        self.step.wait_for_element(self.coordinator_input_field_dropdown, 10)
        self.step.click_element_containing_text(self.coordinator_input_field_dropdown, text)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search)



class RecruitmentAddCandidate:
    first_name = '#addCandidateForm_firstName'
    last_name = '#addCandidateForm_lastName'
    email = '#addCandidateForm_email'
    input_file = '#addCandidateForm_file'
    save_button = "button[type='submit']"
    loading_spinner = 'div[class="oxd-loading-spinner"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd


    def set_first_name(self, text):
        self.step.input_text(self.first_name, text)

    def set_last_name(self, text):
        self.step.input_text(self.last_name, text)

    def set_email(self, text):
        self.step.input_text(self.email, text)

    def upload_resume(self, file_path):
        file_input = self.wd.find_element(By.CSS_SELECTOR, self.input_file)
        file_input.send_keys(file_path)

    def click_save(self):
        self.step.click_on_element(self.save_button)
        self.step.specified_element_is_not_present(self.loading_spinner)

class TrainingAddCourse:
     training_add_title_input_field = 'input[name="addCourse[title]"]'
     coordinator_input_field = 'input[placeholder="Type for hints..."]'
     coordinator_input_field_dropdown = 'div[class="ac_results"] li'
     save_button = 'a[id="btnSaveCourse"]'
     coordinator_input_field_mis = '#addCourse_coordinator_empName-error'

     def __init__(self, step: StepHelper, wd: WebDriver):
         self.step = step
         self.wd = wd

     def set_title(self,text):
         self.step.input_text(self.training_add_title_input_field, text)

     def set_coordinator(self,text):
         self.step.input_text(self.coordinator_input_field, text)
         self.step.wait_for_element(self.coordinator_input_field_dropdown, 5)
         if self.step.specified_element_is_present(self.coordinator_input_field_mis, 5) == False:
             self.step.click_element_containing_text(self.coordinator_input_field_dropdown, text)

     def click_save(self):
         self.step.click_on_element(self.save_button)


class RecruitmentAtsFilter:
    search_button = 'button[type="submit"]'
    from_date_calendar = '(//div[@class="oxd-date-input-icon-wrapper"])[1]'
    header_filter_candidates = 'h5[class="modal-title"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.OXD)

    def click_search_button(self):
        self.step.click_on_element(self.search_button)

    def click_date_applied_from(self):
        self.step.click_on_element(self.from_date_calendar)

    def wait_for_displayed(self):
        self.step.wait_for_element(self.header_filter_candidates)