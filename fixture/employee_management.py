
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    list_of_configurations_texts = "//a[@ng-if='!menu.children && !!menu.uiSref && maxLevels <= 0']"


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table2 = Table(step,
                           row_selector='#employeeListTable tr',
                           column_selectors={'employee_id': 'td:nth-child(2)',
                                             'name': 'td:nth-child(3)',
                                             'job title': 'td:nth-child(4)',
                                             'employment status': 'td:nth-child(5)'
                                             })

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def get_widgets_configurations(self):
        return self.step.get_elements_texts(self.list_of_configurations_texts)