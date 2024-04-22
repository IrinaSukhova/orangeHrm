import time
from fixture.table import Table
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    gear_button = "(//i[text()='ohrm_settings'])[2]"
    my_widgets_tab = "span[class='nav-link active']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    list_of_configurations_texts = "//a[@ng-if='!menu.children && !!menu.uiSref && maxLevels <= 0']"
    list_widgets_names = "span[class='oxd-switch-label']"
    first_table_row = "tbody tr:nth-child(1)"
    list_employee_button = "//a[@class='top-level-menu-item active']"
    filter_button = "a[class='employee-navbar-button action-icon']"


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(
            step,
            row_selector='#employeeListTable tbody tr',
            column_selectors={'employee_id': 'td:nth-child(2)', 'employee_name': 'td:nth-child(3)', 'job_title': 'td:nth-child(4)', 'employment_status': 'td:nth-child(5)'})

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def click_employee_list(self):
        self.step.click_element_by_text(self.list_employee_button, 'Employee List')

    def click_gear_button(self):
        self.step.click_on_element(self.gear_button)

    def click_my_widgets_tab(self):
        self.step.click_on_element(self.my_widgets_tab)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def get_widgets_names(self):
        return self.step.get_elements_texts(self.list_widgets_names)

    def wait_for_table1(self):
        self.step.wait_for_element(self.first_table_row, 40)

    def click_on_filter_button(self):
        self.step.click_on_element(self.filter_button)