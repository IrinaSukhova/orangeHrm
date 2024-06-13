import os
import time

from selenium.webdriver.remote.webdriver import WebDriver

from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from helpers.utils import Utils
from fixture.table import Table

class Attendance:
    set_header = '.report-header-truncate'
    spiner = '.oxd-circle-loader'
    pay_period_dropdown_button = 'div[filter-name="period"] .form-group .input-group-append'
    pay_period_dropdown_value = '//div[@class="dropdown-menu show"]//li//span'
    employee_name_field = 'oxd-multiselect[items="employeesForMultiSelect"] input[autocomplete="off"]'
    employee_name_value = '//ul[@id="dropdown-multyselect"]//li//span[@class="multi-select-title"]'
    csv_button = 'button[data-icon="ohrm_file_csv"]'
    table_present = '#pim_report_table'
    input_supervisor_name = '#report_multiselect_supervisorfilter_supervisors input'
    supervisor_dropdown_value = '#report_multiselect_supervisorfilter_supervisors ul'
    input_job_title = '#report_multiselect_filter_job_title input'
    job_title_dropdown_value = '#report_multiselect_filter_job_title span'
    data_format = 'button[data-id="report_select_filter_data_format"]'
    data_format_value = '#bs-select-4 span'
    input_include = 'button[data-id="report_select_filter_include"]'
    include_dropdown_value = '#bs-select-3 span'
    checkbox = '.custom-control-label'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.OXD)
        self.table = Table(step,
                           row_selector='tr[ng-repeat="result in vm.formattedResults"]',
                           column_selectors={'employee_id': 'td[ng-repeat="value in result track by $index"]:nth-child(1)',
                                             'employee_name': 'td[ng-repeat="value in result track by $index"]:nth-child(2)',
                                             'supervisor': 'td[ng-repeat="value in result track by $index"]:nth-child(3)',
                                             'regular_time': 'td[ng-repeat="value in result track by $index"]:nth-child(4)',
                                             'extra_time': 'td[ng-repeat="value in result track by $index"]:nth-child(5)',
                                             'total_leave_time': 'td[ng-repeat="value in result track by $index"]:nth-child(6)',
                                             'total_time': 'td[ng-repeat="value in result track by $index"]:nth-child(7)',
                                             'status': 'td[ng-repeat="value in result track by $index"]:nth-child(8)' })

    def wait_page_load(self):
        self.step.specified_element_is_not_present(self.spiner, 20)

    def  get_list_of_headers(self):
        return self.step.get_elements_texts(self.set_header)

    def new_pay_period(self, text):
        self.step.click_on_element(self.pay_period_dropdown_button)
        self.step.click_element_by_text(self.pay_period_dropdown_value, text, True)

    def enter_employee_name(self, text):
        self.step.click_on_element(self.employee_name_field, True)
        self.step.input_text(self.employee_name_field, text)
        time.sleep(5)
        self.step.click_element_containing_text(self.employee_name_value, text)

    def export_to_csv(self):
        self.step.click_on_element(self.csv_button)
        # Wait for the download to complete (you may need to adjust the sleep duration)
        self.step.specified_element_is_not_present(self.spiner, 20)
        time.sleep(3)  # Additional sleep to ensure download completes
        # Check the download directory for the downloaded file
        download_path = os.path.join(Utils.get_project_root(), 'files', 'download')
        downloaded_files = os.listdir(download_path)
        if len(downloaded_files) == 0:
            raise Exception("No files were downloaded.")


    def table_is_present(self):
        self.step.specified_element_is_present(self.table_present, 20)

    def enter_supervisor_name(self, text):
        self.step.click_on_element(self.input_supervisor_name)
        self.step.input_text(self.input_supervisor_name, text)
        self.step.wait_for_element(self.input_supervisor_name)
        time.sleep(1)
        self.step.click_element_containing_text(self.supervisor_dropdown_value, text)

    def set_job_title(self, text):
        self.step.click_on_element(self.input_job_title)
        self.step.input_text(self.input_job_title, text)
        self.step.wait_for_element(self.input_job_title)
        time.sleep(1)
        self.step.click_element_containing_text(self.job_title_dropdown_value, text)

    def set_data_format(self, text):
        self.step.click_on_element(self.data_format)
        time.sleep(1)
        self.step.click_element_containing_text(self.data_format_value, text)

    def set_include(self, text):
        self.step.click_on_element(self.input_include)
        self.step.click_element_containing_text(self.include_dropdown_value, text)

    def click_checkbox(self):
        self.step.click_on_element(self.checkbox)

    def scroll_to_table_headers(self):
        self.step.scroll_element_into_center(self.set_header)