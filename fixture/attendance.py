import os
import time

from selenium.webdriver.remote.webdriver import WebDriver

from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from helpers.utils import Utils
from fixture.table import Table

class Attendance:
    set_header = '.report-header-truncate'
    spiner = 'div[class="oxd-circle-loader"]'
    pay_period_dropdown_button = 'div[filter-name="period"] .form-group .input-group-append'
    pay_period_dropdown_value = '//div[@class="dropdown-menu show"]//li//span'
    employee_name_field = 'oxd-multiselect[items="employeesForMultiSelect"] input[autocomplete="off"]'
    employee_name_value = '//ul[@id="dropdown-multyselect"]//li//span[@class="multi-select-title"]'

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

    def wait_page_present(self):
        self.step.specified_element_is_not_present(self.spiner, 20)

    def  get_list_of_headers(self):
        self.step.specified_element_is_not_present(self.set_header)
        time.sleep(3)
        return self.step.get_elements_texts(self.set_header)

    def new_pay_period(self, text):
        self.step.click_on_element(self.pay_period_dropdown_button)
        self.step.click_element_by_text(self.pay_period_dropdown_value, text, True)

    def enter_employee_name(self, text):
        self.step.click_on_element(self.employee_name_field, True)
        self.step.input_text(self.employee_name_field, text)
        self.step.click_element_containing_text(self.employee_name_value, text)
